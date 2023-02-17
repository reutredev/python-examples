import time
from functools import update_wrapper
import types
from sqlalchemy.exc import SQLAlchemyError, ArgumentError, OperationalError
import logging

logger = logging.getLogger(__name__)

db_retry_intervals = [0, 0.5, 1]


class RetrySession:
    # Note: a function that is decorated by this decorator should raise and not swallow SQLAlchemyErrors
    # that are related to network/connection errors in order to allow retry mechanism.
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func
        self.sleep_per_attempt = db_retry_intervals
        self.max_retries = len(self.sleep_per_attempt)
        self.max_attempts = self.max_retries + 1

    def __get__(self, instance, owner):
        if instance is None:
            return self  # Accessed from class, return unchanged
        return types.MethodType(self, instance)  # Accessed from instance, bind to instance

    def sleep_before_retry(self, attempts):
        time_to_sleep = self.sleep_per_attempt[attempts]
        logger.warning(
            f"DB query error in {self.func.__name__}(), attempt#: {attempts + 1} out of {self.max_attempts}. "
            f"Retrying in {time_to_sleep} seconds")

        time.sleep(time_to_sleep)

    def handle_sql_exception(self, attempts, session):
        if attempts >= self.max_retries:
            logger.error(
                f"DB query error in {self.func.__name__}(), number of attempts is {self.max_attempts}, "
                f"raising exception")
            raise
        session.rollback()
        self.sleep_before_retry(attempts)

    def __call__(self, obj, *args, **kwargs):
        if 'session' in kwargs:
            session = kwargs['session']
        else:
            session = obj.session

        max_attempts = self.max_retries + 1
        attempts = 0

        while attempts < max_attempts:
            try:
                return self.func(obj, *args, **kwargs)
            except ArgumentError as err:
                print(repr(err))
                raise
            except SQLAlchemyError as err:
                print(repr(err))
                self.handle_sql_exception(attempts=attempts, session=session)
                attempts += 1


# def retry_session_with_retry_or_return(to_return_on_exp):
#     # Following exists mainly to allow backward compatibility for functions that return default value instead of throwing exception.
#     def decorate(func):
#         first_wrap = RetrySession(func)
#
#         def inner(*args, **kwargs):
#             try:
#                 return first_wrap(*args, **kwargs)
#             except OperationalError:
#                 return to_return_on_exp
#         return inner
#     return decorate


retry_session = RetrySession

if __name__ == '__main__':  # pragma: no cover
    pass

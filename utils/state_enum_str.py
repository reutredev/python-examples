from enum import Enum
from functools import lru_cache


class ProcessState(str, Enum):
    FAILURE = 'fail'
    COMPLETED = 'completed'
    IN_PROGRESS = 'in-progress'
    ABORTED = 'aborted'
    FAIL_TIMEOUT = 'fail-timeout'
    CREATED = 'created'
    EXCEPTION = 'exception'

    def __str__(self):
        return self.value

    @staticmethod
    def final_states():
        return [ProcessState.FAILURE, ProcessState.COMPLETED, ProcessState.ABORTED, ProcessState.FAIL_TIMEOUT,
                ProcessState.EXCEPTION]

    @staticmethod
    @lru_cache()
    def final_states_str():
        return [str(v) for v in ProcessState.final_states()]

    def is_final_state(self) -> bool:
        return self in ProcessState.final_states()

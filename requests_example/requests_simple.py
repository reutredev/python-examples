import requests


class HttpTest:
    def __init__(self):
        self.session = requests.session()
        self.headers = {
            'Content-Type': 'application/json'
        }
        self.base_url = "http://httpbin.org"

    def http_get(self, url, params):
        try:
            full_url = self.base_url + "/" + url
            response = self.session.get(url=full_url, params=params, headers=self.headers, timeout=120)
            res_json = response.json()
            print(f"status_code = {response.status_code}")
            assert response.status_code == 200, f"{response.status_code} == 200"
            print(res_json)
        except Exception as e:
            print(f"Exception is: {e}")

    def http_post(self, url, req_data):
        try:
            full_url = self.base_url + "/" + url
            response = self.session.post(url=full_url, json=req_data, headers=self.headers, timeout=120)
            #response = self.session.post(url=full_url, data=data)
            res_json = response.json()
            print(f"status_code = {response.status_code}")
            assert response.status_code == 200, f"{response.status_code} == 200"
            print(res_json)
        except Exception as e:
            print(f"Exception is: {e}")

    def http_get_proxy(self, url, params, proxies):
        try:
            full_url = self.base_url + "/" + url
            response = self.session.get(url=full_url, params=params, headers=self.headers, timeout=120, proxies=proxies)
            res_json = response.json()
            print(f"status_code = {response.status_code}")
            assert response.status_code == 200, f"{response.status_code} == 200"
            print(res_json)
        except Exception as e:
            print(f"Exception is: {e}")


if __name__ == '__main__':
    http_test = HttpTest()
    data = {
        "name": "my_name",
        "age": 25
    }
    http_test.http_get("get", data)
    http_test.http_post("post", data)
    proxies = {
        "http": "139.99.237.62:80",
        "https": "139.99.237.62:80"
    }
    http_test.http_get_proxy("get", data, proxies)


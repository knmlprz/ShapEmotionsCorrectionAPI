from locust import HttpUser, task


class WebsiteUser(HttpUser):
    @task
    def short_sentiment(self):
        self.client.post("/sentiment", json={"value": "Hello, hi, how are you"})

    @task
    def long_sentiment(self):
        self.client.post(
            "/sentiment",
            json={
                "value": "Hello, hi, how are you. I really "
                "like you. How about a test, lets see how this api"
                "handles big loads of data."
            },
        )

    @task
    def short_sentiment(self):
        self.client.post("/sentiment/explain", json={"value": "Hello, hi, how are you"})

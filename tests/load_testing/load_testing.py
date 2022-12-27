from locust import HttpUser, between, task


class WebUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def load_main(self):
        self.client.post("/predict", json=
        {
        "number_vmail_messages": 3,
        "total_day_calls": 4,
        "total_eve_minutes": 2,
        "total_eve_charge": 12,
        "total_intl_minutes": 1,
        "number_customer_service_calls": 10
        }
        )
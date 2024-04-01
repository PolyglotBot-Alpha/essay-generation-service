import requests
import time


class CircuitBreaker:
    def __init__(self, failure_threshold=3, recovery_timeout=60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failures = 0
        self.state = "CLOSED"
        self.last_failure_time = None

    def record_success(self):
        self.state = "CLOSED"
        self.failures = 0

    def record_failure(self):
        self.failures += 1
        if self.failures >= self.failure_threshold:
            self.state = "OPEN"
            self.last_failure_time = time.time()

    def can_execute(self):
        if self.state == "CLOSED":
            return True
        elif self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_timeout:
                # After the recovery timeout, allow one attempt to see if the issue is resolved
                self.state = "HALF-OPEN"
                return True
            else:
                return False
        elif self.state == "HALF-OPEN":
            # Allow the service to be called in HALF-OPEN state to test if the service has recovered
            return True

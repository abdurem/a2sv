class Solution:
    def maximumRequests(self, n, requests):
        for num_requests in range(len(requests), 0, -1):
            for request_combination in itertools.combinations(range(len(requests)), num_requests):
                degree = [0] * n
                for req_index in request_combination:
                    degree[requests[req_index][0]] -= 1
                    degree[requests[req_index][1]] += 1
                if not any(degree):
                    return num_requests
        return 0
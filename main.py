from slidingwindow import SldingWindow
from tokenbucket import TokenBucket
from ratelimiter import RateLimit

# Test 1: each user may make 3 requests every 10 seconds
print("Test 1: 3 requests per 10 seconds")
limiter = RateLimit(SldingWindow(3, 10))
print("second 0 :", limiter.allow("Alice", 0))
print("second 1 :", limiter.allow("Alice", 1))
print("second 2 :", limiter.allow("Alice", 2))
print("second 3 :", limiter.allow("Alice", 3))
print("second 9 :", limiter.allow("Alice", 9))
print("second 10:", limiter.allow("Alice", 10))

# Test 2: token bucket, 3 tokens, 1 new token every second
print("Test 2: token bucket (3 tokens, 1 new token per second)")
limiter = RateLimit(TokenBucket(3, 1))
print("second 0, request 1:", limiter.allow("Bob", 0))
print("second 0, request 2:", limiter.allow("Bob", 0))
print("second 0, request 3:", limiter.allow("Bob", 0))
print("second 0, request 4:", limiter.allow("Bob", 0))
print("second 1, request 1:", limiter.allow("Bob", 1))
print("second 1, request 2:", limiter.allow("Bob", 1))
print("second 4, request 1:", limiter.allow("Bob", 4))

# Test 3: every user has their own count
print("Test 3: two users, 2 requests per 5 seconds")
limiter = RateLimit(SldingWindow(2, 5))
print("Shashi, second 6 :", limiter.allow("Shashi", 6))
print("Shashi, second 6 :", limiter.allow("Shashi", 6))
print("Shashi, second 6 :", limiter.allow("Shashi", 6))
print("Priya, second 6  :", limiter.allow("Priya", 6))
print("Shashi, second 11:", limiter.allow("Shashi", 11))
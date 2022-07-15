from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class UserThrottle(UserRateThrottle):
	scope = "user"
	rate = "10000/day"


class AnonThrottle(AnonRateThrottle):
	scope = "anon"
	rate = "50/day"


class AnonRegThrottle(AnonRateThrottle):
	scope = "anon_reg"
	rate = "10/day"


class FreeBehavior(UserThrottle):
	scope = "free"
	rate = "1_000_000/day"

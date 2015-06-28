class Poll:
    def __init__(self):

    def poll(self, call, check, timeout):
        result = call()
        if check(result)

    def timeout(func, args=(), kwargs={}, timeout_duration=1, default=None):
        ''' see http://stackoverflow.com/questions/492519/timeout-on-a-python-function-call '''
        import signal

        class TimeoutError(Exception):
            pass

        def handler(signum, frame):
            raise TimeoutError()

        # set the timeout handler
        signal.signal(signal.SIGALRM, handler) 
        signal.alarm(timeout_duration)
        try:
            result = func(*args, **kwargs)
        except TimeoutError as exc:
            result = default
        finally:
            signal.alarm(0)

        return result
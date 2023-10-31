from source.helpers.decorators.singleton import singleton, thread_safe_singleton


def test_singleton():
    @singleton
    class SingletonClass:
        def __init__(self, value):
            self.value = value

    instance1 = SingletonClass("first")
    instance2 = SingletonClass("second")

    assert instance1 is instance2

    assert instance1.value == "first"
    assert instance2.value == "first"


def test_thread_safe_singleton():
    @thread_safe_singleton
    class ThreadSafeSingletonClass:
        def __init__(self, value):
            self.value = value

    instance1 = ThreadSafeSingletonClass("first")
    instance2 = ThreadSafeSingletonClass("second")

    assert instance1 is instance2

    assert instance1.value == "first"
    assert instance2.value == "first"


def test_singleton_no_args():
    @singleton
    class SingletonNoArgs:
        def __init__(self):
            self.value = "no_args"

    instance1 = SingletonNoArgs()
    instance2 = SingletonNoArgs()

    assert instance1 is instance2
    assert instance1.value == "no_args"


def test_thread_safe_singleton_no_args():
    @thread_safe_singleton
    class ThreadSafeSingletonNoArgs:
        def __init__(self):
            self.value = "no_args"

    instance1 = ThreadSafeSingletonNoArgs()
    instance2 = ThreadSafeSingletonNoArgs()

    assert instance1 is instance2
    assert instance1.value == "no_args"

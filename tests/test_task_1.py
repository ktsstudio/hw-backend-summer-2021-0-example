from tasks.task_1 import say_kts


def test_say_kts():
    assert say_kts() == 'kts', 'You should say kts'

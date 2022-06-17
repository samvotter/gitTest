import bar.hello
import foo.world


def test_helloworld():
    hello = bar.hello.Hello()
    world = foo.world.World()
    assert f"{hello} {world}" == "Hello world"

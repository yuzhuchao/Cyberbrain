from cyberbrain import Creation, InitialValue


def test_existing_variable_emit_initial_value(tracer):
    x = "foo"
    tracer.init()
    y = x
    tracer.register()

    assert tracer.events == {
        "x": [InitialValue(target="x", value="foo", lineno=7)],
        "y": [Creation(target="y", value="foo", sources={"x"}, lineno=7)],
    }
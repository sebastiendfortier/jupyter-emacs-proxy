def test_setupcall():
    """
    Test the call of the setup function
    """
    import os
    import jupyter_gui_app_proxy as js

    os.environ["XPRA_BIN"] = "xpra"

    print("\nRunning test_setupcall...")
    print(js.setup_gui_app())

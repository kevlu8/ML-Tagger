class TestMain():
    def test_convert(self, tmpdir):
        import main
        import PIL.Image
        import os
        import tempfile
        a, b, c, d = os.path.join(tmpdir, "big.jpg"), os.path.join(tmpdir, "big.png"), os.path.join(tmpdir, "small.jpg"), os.path.join(tmpdir, "small.png")
        PIL.Image.new("RGB", (main.MAX_HEIGHT * 2, main.MAX_WIDTH * 2)).save(a)
        PIL.Image.new("RGB", (main.MAX_HEIGHT * 2, main.MAX_WIDTH * 2)).save(b)
        PIL.Image.new("RGB", (main.MAX_HEIGHT, main.MAX_WIDTH)).save(c)
        PIL.Image.new("RGB", (main.MAX_HEIGHT, main.MAX_WIDTH)).save(d)
        main.convertAndScale((a, a))
        assert main.eventQueue[0][0] == "convertAndScale finished"
        f = main.eventQueue[0][1]["filename"]
        assert f[1] == a
        assert f[0] != a
        assert f[0].startswith(tempfile.tempdir)
        assert PIL.Image.open(f[0]).size == (main.MAX_WIDTH, main.MAX_HEIGHT)
        main.convertAndScale((b, b))
        f = main.eventQueue[0][1]["filename"]
        assert f[1] == b
        assert f[0] != b
        assert f[0].startswith(tempfile.tempdir)
        assert PIL.Image.open(f[0]).size == (main.MAX_WIDTH, main.MAX_HEIGHT)
        main.convertAndScale((c, c))
        f = main.eventQueue[0][1]["filename"]
        assert f[1] == c
        assert f[0] != c
        assert f[0].startswith(tempfile.tempdir)
        assert PIL.Image.open(f[0]).size == (main.MAX_WIDTH, main.MAX_HEIGHT)
        main.convertAndScale((d, d))
        f = main.eventQueue[0][1]["filename"]
        assert f == (d, d)
        assert PIL.Image.open(f[0]).size == (main.MAX_WIDTH, main.MAX_HEIGHT)

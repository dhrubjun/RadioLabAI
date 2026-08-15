from radiolab_ai.__main__ import main


def test_main_prints_app_name(capsys):
    main()

    captured = capsys.readouterr()

    assert captured.out.strip() == "RadioLab AI V1"
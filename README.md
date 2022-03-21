# One-Dimensional Agent Model

## type annotiation

- Callable  
  [references]: https://docs.python.org/3/library/typing.html#callable

Frameworks expecting callback functions of specific signatures might be type hinted using `Callable[[Arg1Type, Arg2Type], ReturnType]`.

## 仮想環境の整備

1. 仮想環境作成 : python3 -m venv .venv
2. 仮想環境に入る : source .venv/bin/activate
3. 依存環境の整備 : python3 -m pip install -r requirements.txt
4. 仮想環境から抜ける : deactivate

- requirements.txt を作成する python3 -m pip freeze > requirements.txt

- 仮想環境内にパッケージをインストール python3 -m pip install requests python3 -m ppip install selenium

## 結果

[Link](report/report.md)
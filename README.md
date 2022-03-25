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

- 仮想環境内にパッケージをインストール python3 -m pip install requests python3 -m pip install selenium

## 結果

実装の関係上、初期状態は[-1, 1]の一様分布としている。
詳しい実装は[こちら](./main.py)

[Link](report/report.md)

## 参考資料(Web サイト等)

- matplotlib

  - histgram  
    `matplotlib.pyplot.hist(x, bins=None, range=None, density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, normed=None, **kwargs)`がとりうる引数の説明一覧

    [references](https://pythondatascience.plavox.info/matplotlib/%E3%83%92%E3%82%B9%E3%83%88%E3%82%B0%E3%83%A9%E3%83%A0)

  - xlim, ylim による描画範囲の設定
    ```python
    plt.xlim(-2, 12)
    plt.ylim(-1.5, 1.5)
    ```
    のようにするだけ、[reference](https://tech.nkhn37.net/matplotlib-plot-lim-axis/)

- markdown の画像リサイズ  
  `![***代替テキスト***](***画像のURL***)`  
  ではなく  
  `<img src="***画像のURL***" width="***サイズ***">`  
  を用いる  
  [references](https://qiita.com/shti_f/items/b819d7fd8cb79ae29687)

- 擬似正規分布

  [references](https://teratail.com/questions/271907)

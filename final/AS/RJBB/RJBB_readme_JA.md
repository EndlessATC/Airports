# `RJBB` 進入管制区 4.0.0

> 作者は日本人ではありません。以下の文章には間違っている日本語、または間違っている情報が含まれている場合があります。ご了承いただければ幸いです。

KANSAI ACA(関西進入管制区)を[Endless ATC](https://steamcommunity.com/app/666610)に追加するMODです。`RJBB`関西国際空港、`RJOO`大阪国際空港(伊丹)、`RJBB`神戸空港、`RJOS`徳島空港、`RJOT`高松空港、`RJOB`岡山空港、そして`RJOY`八尾空港が再現されています. 空域の上限はFL180です.

AIP Japan 2021/08/12 （国土交通省） (https://aisjapan.mlit.go.jp/) をもとに作成しています。 再現されているSID及びSTARは現実の運用と異なる場合があるかもしれませんが、基本的に日中の景気気象状態 (IMC) を再現しているつもりです。すべての航空機がRNAV対応としていて、RNAVの代わりがない場合を除き非RNAVのSID及びSTARは実装されていません。海岸のデータは[naturalearthdata.com](http://www.naturalearthdata.com)のを使っています。

STARはこのゲームの進入方式で再現されています。進入方式に従って飛行することをを許可できる飛行機は有効なポイントに向かっていなければなりません。友好のポイントにDCTの指示を出した後、ILSの指示の代わりにAPP指示を出せます。一つのポイントから複数の進入方式が始まる場合もあります。指示を確定する前にまたAPPのボタンをクリック/キーを押すと次の進入方式に変わります。選択している飛行機がすでに進入方式に従って飛行しているならば、いったんDCTでポイントに向かう指示を選択しなければ飛行方式の変更はできません。

KANSAI ACAの南部の直下にあるTOKUSHIMA ACA (徳島進入管制区)はゲームの仕様上、KANSAI ACAの一部として実装しています。`RJOS`発着便のみTOKUSHIMA ACA （`OS`の表示がある空域）に入れます。

高知空港とその周辺の空域はゲームの仕様上実装するのは困難なため、省略されています. `RJOO`/`RJBB`発着の`RJOK`便もゲームの仕様上再現できません。

## 登場する空港

### `RJBB` 関西国際空港

到着機は管制区に入った後、フライトプランルートに沿って進んで、終点ポイントにたどり着いたら新たな指示がない場合ホールドに入る。STARと進入許可はルートの各ポイントから出せる。STARも途中のポイントから再開の指示を出せて、進入許可もIAF/IFあるいはFAFから出せる。ルート終点ポイントとその到着ルートは以下の通り:

- `ALISA` 
	- `Y36 ALISA`: `TONBI SAEKI ALISA` (北西)
	- `Y361 SAEKI Y36 ALISA`: `SPICE SAEKI ALISA` (北東)
- `BERTH` 
	- `Y35 BERTH`: `(Y35) RANDY BERTH` (西)
- `BECKY`
	- `Y53 BECKY`: `KARIN BECKY` (南西)
- `CANDY`
	- `Y46 CANDY`: `EVERT CANDY` (南南西、南、東)
- `DANDE`
	- `Y544 DANDE`: `(Y544) SINGU RIDGE DANDE` (`RJTT`/`RJAA`/`RJSS`/`RJSF`)

### `RJOO` 大阪国際空港(伊丹)

到着機は管制区に入った後、フライトプランルートに沿って進んで、終点ポイントにたどり着いたら新たな指示がない場合ホールドに入る。STARと進入許可はルートの各ポイントから出せる。STARも途中のポイントから再開の指示を出せて、進入許可もIAF/IFあるいはFAFから出せる。ルート終点ポイントとその到着ルートは以下の通り:

- `IKOMA` 
	- via `ROKKO`
		- `Y384 ROKKO`: `(Y384) ROKKO` (北東)
		- `Y38 ROKKO`: `TOZAN ROKKO`  (北西)
		- `RJBT.../RJOR YME V55.../RJOH YME V55...ROKKO`: `(GUNZE) ROKKO` (`RJBT`/`RJOR`/`RJOH`)
		- `ROKKO`からのSTARはフライトプランルートに含まれるので`ROKKO`から`ROKKO KAMEO OTABE ABENO IKOMA`を沿って`IKOMA`まで進む
	- via `KODAI`
		- `Y546 KODAI`: `OHDAI KODAI` (東)
		- `KODAI`からのSTARはフライトプランルートに含まれるので`KODAI`から`KODAI MIRAI ABENO IKOMA`を沿って`IKOMA`まで進む
- `IZUMI`
	- `Y401 KAINA Y753 IZUMI`: `RIVER ZOROH KAZRA MIRIO KAINA IZUMI` (西)
	- `Y231 MIRIO Y401 KAINA Y753 IZUMI`: `(Y231) JANGO BECKY MIRIO KAINA IZUMI` (西)
	- `Y753 IZUMI`: `MUGIE HONMA KAINA IZUMI` -> `HONMA` -> `KAINA` -> `IZUMI` (南西)

### `RJBE` 神戸空港

到着機は管制区に入った後、フライトプランルートに沿って進んで、終点ポイントにたどり着いたら新たな指示がない場合ホールドに入る。STARと進入許可はルートの各ポイントから出せる。STARも途中のポイントから再開の指示を出せて、進入許可もIAF/IFあるいはFAFから出せる。ルート終点ポイントとその到着ルートは以下の通り:

- `TRACY`
	- `Y20 WAKIT Y201 TRACY`: `ARASI GINJI WAKIT TRACY` (東)
	- `Y382 WAKIT Y201 TRACY`: `(Y382) WAKIT TRACY` (北東)
- `BERTH`
	- `Y35 BERTH`: `(Y35) RANDY BERTH` (西)
- `BECKY`
	- `Y53 BECKY`: `(Y53) KARIN BECKY` (南西)

### `RJOS` 徳島空港

到着機は管制区に入った後、フライトプランルートに沿って進んで、終点ポイントにたどり着いたら新たな指示がない場合ホールドに入る。進入許可はルートの各ポイント、IAF、IFあるいはFAFから出せる。ルート終点ポイントとその到着ルートは以下の通り:

- `DATIS`
	- `Y544 SINGU Y542 DATIS`: `SINGU SOMEI DINAH GOBOH UBUYU DATIS` (東)
- `TSC`
	- `KEC JOSIN TSC`: `(KEC30) JOSIN TSC` (南東)
	- `Y33 KTE KULUL TSC`: `SAKAI KOMPI KTE KULUL TSC` (西)

### `RJOT` 高松空港

到着機は管制区に入った後、フライトプランルートに沿って進んで、終点ポイントにたどり着いたら新たな指示がない場合ホールドに入る。STARと進入許可はルートの各ポイントから出せる。STARも途中のポイントから再開の指示を出せて、進入許可もIAF/IFあるいはFAFから出せる。ルート終点ポイントとその到着ルートは以下の通り:

- `WIMPY`
	- `Y20 WAKIT Y203 WIMPY` (東)
- `KTE`
	- `Y288 TAKMA KTE`: `TAKMA KTE` (西)
	- `Y39 OYE KTE`: `YUBAR OYE KTE` (北西)

### `RJOB` 岡山空港

到着機は管制区に入った後、フライトプランルートに沿って進んで、終点ポイントにたどり着いたら新たな指示がない場合ホールドに入る。進入許可はルートの各ポイント、IAF、IFあるいはFAFから出せる。ルート終点ポイントとその到着ルートは以下の通り:

- `OYE`
	- `Y20 WAKIT Y205 OYE`: `ARASI GINJI WAKIT TRIPY MIMMY SIMAG BENES OYE` (東)
	- `Y382 WAKIT Y205 OYE`: `(Y382) WAKIT TRIPY MIMMY SIMAG BENES OYE` (北東)
	- `Y39 OYE`: `YUBAR OYE` (北西)
	- `Y288 INOOK OYE`: `TAKMA INOOK OYE` (西)

### `RJOY` 八尾空港

到着機は管制区に入った後、フライトプランルートに沿って進んで、終点ポイントにたどり着いたら新たな指示がない場合ホールドに入る。進入許可はルートの各ポイント、IAF、IFあるいはFAFから出せる。ルート終点ポイントとその到着ルートは以下の通り:

- `IZUMI`
	- `V28 ITE V55 IZUMI`: `MIDER ITE IZUMI` (東)
	- `(YME) V55 IZUMI`: `GUNZE ROKKO SANDA ITE IZUMI` (北)
	- `Y384 ROKKO V55 IZUMI`: `(Y384) ROKKO SANDA ITE IZUMI` (北東)
	- `Y38 ROKKO V55 IZUMI`: `TOZAN ROKKO SANDA ITE IZUMI` (北西)
	- `(KRE) KAIFU IZARI MIKAN IZUMI`: `KAIFU IZARI MIKAN IZUMI` (南西)
	- `V28 ITE V55 IZUMI`: `WASYU OYE OLIVE AYAYA BUMER ARIMA ITE IZUMI` (西)
	- `Y33 KTE KULUL TSC MIKAN IZUMI`: `SAKAI KOMPI KTE KULUL TSC MIKAN IZUMI` (西)
	- `V55 IZUMI`: `NORAN OSAMU IYOKA IZUMI` (南東)

## 既知の問題点

- 旋回進入はエクステンドダウンウィンドをする（ゲームの仕様で短いファイナルはできないため）
- `Y401`から`RJOO`の到着機は`DH8D`に限定されていない (ゲームの仕様ではできない)
- `KAIFU` から`RJOO` の到着機はその他プロップ機に限定されていない (ゲームの仕様ではできない)

## 変更履歴

*	3.0.0 - 2021/05/24
	- ソースをリライト
		- 現実にはない高度制限を削除
			- 到着機が高い速度と高度で`OHDAI`に出現するので`KODAI`にFL130/250kt制限を設定
		- 旋回侵入を一新
			- `RJOO` 14s
				- `UMEDA`でleft break
			- `RJOT` 08
			- `RJOS` 11
			- `RJBE` 27
				- およそ5DMEでright break
				- 27 到着機はダウンウィンドに合流するまで高度2500以上を維持します
					- ダウンウィンドで1500に降下して、直上の高度2600に降下する`RJBB`到着機からのセパレーションを維持します
					- ベースターンで高度2600以下に降下し始める`RJBB`到着機とのセパレーションを失わないようになりました
				- 27出発機は27到着木の下の高度1500ですれ違って`MAIKO`へ向かえるようになりました
					- o到着機までの距離に余裕がある場合、まず高度5000に上昇して到着機の上を`MAIKO`に向かうことも可能
		- `RJBB` ILS Y 進入を実装
		- `RJOO` 到着機の　`MIRIO`, `JANGO` 出現ポイントを修正
		- `RJOO` RNAV 32L 進入を実装
		- 使用滑走路の組み合わせを一つ追加
		- `RJOO`出発経路を大幅に修正
			- 32Rから`ASUKA`へ向かう出発機は離陸後右に旋回しないように修正
			- `ITE` ラジアルによる出発経路が磁気偏角を配慮していなかったことを修正
			- `FOSTA` TRANSITIONを実装
		- `RJBB`出発経路を大幅に修正
			- Fly-overポイントを通過してから旋回するように修正
			- 24Lから`KNE`へ向かう出発機が離陸後左に旋回しないように修正
		- 制限空域(特別管制区など)の形を改良
	- `CUE` 大津VORDMEを廃止
		- 代わりに`MIDER`を設定
		- `RJOO` OTSU FIVE DEPARTUREとKOMATSU TRANSITIONを廃止
		- `RJOO` PANAS ONE DEPARTUREとKOMAZ TRANSITIONを設定
		- `RJBE` OTSU TRANSITIONを廃止
		- `RJBE` MIDER TRANSITIONを設定
	- `RJOY` 八尾空港を実装
		- 09-27滑走路だけ実装
		- これに伴い小型機を大量実装
*	3.1.0 - 2021/07/02
	- ハンドオフ先のコールサイン及び周波数を実装
	- 徳島の発音を改良
*	4.0.0 - 2021/08/30
	- 到着経路をリニューアル
		- 到着機はフライトプランルートの終点まで進む
		- 到着機が管制区に入る位置を修正
		- 到着機が管制区に入る時の高度を各ルートで設定
		- `RJBB`
			- `ALISA`からの到着機は`Y36`と`Y361`を別々にエントリーポイントを設定
		- `RJOO`
			- 各スポーンポイントの交通量比率を調整
			- 山陰地区空港からのエントリーポイントを設定
		- `RJOY`
			- エントリーポイントを変更
	- 登場機をアップデート
		- 比率を調整
			- `RJBB`, `RJBE`, `RJOT`, `RJOB`の小型機の比率を下げる
		- `RJBE`, `RJOT`, `RJOB`に小型機を実装
		- `CYGNS`をアップデート、`RJOO`に`JF1`と`AF1`を実装
		- `RJOS`に所在しない自衛隊機を追加
		- チェックスターを追加
	- `RJBE`27に旋回する到着機とセパレーションのため`RJBB` ILS Z/Y 24R アプローチを調整
	- `B763`がミスドアプローチしないように`RJBE`27への旋回経路を調整
	- 出発機の一次上昇高度を各出発経路に設定
		- 特に`RJBE`09出発機は1500までの上昇に対して27出発機は3000まで上昇する
		- `RJBE`西風の時の西行量が大福に減る
	- 出発経路の名前を変更
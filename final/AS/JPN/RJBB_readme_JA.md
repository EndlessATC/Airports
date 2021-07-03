# `RJBB` 進入管制区 3.1.0

＊作者は日本人ではありません。以下の文章には間違っている日本語、または間違っている情報が含まれている場合があります。ご了承いただければ幸いです。

KANSAI ACA(関西進入管制区)を[Endless ATC](https://steamcommunity.com/app/666610)に追加するMODです。`RJBB`関西国際空港、`RJOO`大阪国際空港(伊丹)、`RJBB`神戸空港、`RJOS`徳島空港、`RJOT`高松空港、`RJOB`岡山空港、そして`RJOY`八尾空港が再現されています. 空域の上限はFL180です.

AIP Japan 2021/08/12 （国土交通省） (https://aisjapan.mlit.go.jp/) をもとに作成しています。 再現されているSID及びSTARは現実の運用と異なる場合があるかもしれませんが、基本的に日中の景気気象状態 (IMC) を再現しているつもりです。すべての航空機がRNAV対応としていて、RNAVの代わりがない場合を除き非RNAVのSID及びSTARは実装されていません。海岸のデータは[naturalearthdata.com](http://www.naturalearthdata.com)のを使っています。

STARはこのゲームの進入方式で再現されています。進入方式に従って飛行することをを許可できる飛行機は有効なポイントに向かっていなければなりません。友好のポイントにDCTの指示を出した後、ILSの指示の代わりにAPP指示を出せます。一つのポイントから複数の進入方式が始まる場合もあります。指示を確定する前にまたAPPのボタンをクリック/キーを押すと次の進入方式に変わります。選択している飛行機がすでに進入方式に従って飛行しているならば、いったんDCTでポイントに向かう指示を選択しなければ飛行方式の変更はできません。

KANSAI ACAの南部の直下にあるTOKUSHIMA ACA (徳島進入管制区)はゲームの仕様上、KANSAI ACAの一部として実装しています。`RJOS`発着便のみTOKUSHIMA ACA （`OS`の表示がある空域）に入れます。

ゲームの仕様上、快適に遊べるように本作ではKANSAI ACAの空域を`OHDAI`の周りに中部へ、または`ROKKO`と`WAKIT`の周りに北へ拡大しています。高知空港はゲームの仕様上実装するのは困難なため、省略されています. 高知県民には申し訳ございません。`RJOO`/`RJBB`発着の`RJOK`便もゲームの仕様上再現できません。

## 登場する空港

### `RJBB` 関西国際空港

＊未翻訳
The main airport of this airspace, Kansai handles both domestic and international traffic to the Kansai region (Osaka, Kobe, Kyoto, Nara, etc). Arrivals/departures will fly over RJBE Kobe to the north, and care should taken here to maintain separation of aircraft.

There is custom traffic for `RJBB`. The proportions are very much estimates but shouldn't be too far off from reality.

Many fixes visible on the map have a defined hold including some key fixes along the STARs.

Aircraft arrive at:

- (`SAEKI`) -> `ALISA` (northwest from Korea/northern China and northeast from NE Japan, Europe)
- (`RANDY`) -> `BERTH` (west from Fukuoka, western Japan, China)
- (`KARIN`) -> `BECKY` (southwest from southwestern Japan, Taiwan, HK, Singapore, Malaysia, etc.)
- (`EVERT`) -> `CANDY` (southwest from Philippines, south from Indonesia/Oceania, east from Nagoya/PACOTS)
- (`KOHWA`) -> `SINGU` -> `DANDE` (east from RJTT Tokyo, RJAA Narita, RJSS Sendai, RJSF Fukushima)

Aircraft depart via:

- `KEC` (east for `RJAA` Narita, PACOTS)
- `SHTLE` (east for `RJTT` Tokyo)
- `UENOH` (northeast to Tohoku, southeast Hokkaido)
- `SIGAK` (northeast to northwest Hokkaido, east NA, Europe)
- `YME` (northeast to northeastern China)
- `SOUJA` (northwest to Korea, northern China, Europe)
- `WASYU` (west to western Japan/Jeju)
- `HABAR` (west to China)
- `POPPY` (southwest to Taiwan, HK, Singapore, Malaysia, etc.)

There are two runways:

- 06R/24L (RWY A)
- 06L/24R (RWY B)

Note that simultaneous parallel independent approaches do not appear to be in use at RJBB. It is possible in the game, but the approaches are not built with this in mind. Of course, you can still do simultaneous parallel dependent approaches with staggered sequencing, which can help with dealing with wake turbulence separation.

The preferred runway is generally RWY A as the main terminal 1 is much closer to RWY A. LCC carriers operating from terminal 2 would have a shorter taxi from RWY B.

STARs are available from `ALISA`, `BERTH`, `BECKY`, `CANDY`, `DANDE`, and approach modes can be activated from those fixes as well as intermediate fixes on the STARs, as well as fixes on airways joining to the STARs.

There are two landing configurations:

-	Landing/departing RWY 06L/06R

This is the preferred configuration for RJBB. 

Vectors can be used for sequencing, or direct to fix shortcuts can also be issued (or both). Approaches are available from `ALLAN` and `BERRY`, and approaches from GATES are available from `JANET` and `JENNY`.

Use care not to descend arrivals into Tokushima ACA. Cross TANTA (from ALISA), NALTO (from BERTH), EVIAN, DATIS, JOLLY +6000 (at or above 6000).

Departures will be climbing over `RJBE` departures from 09, use care to maintain separation. Departures may also join paths after diverging initially especially after `MAIKO`, and may conflict with departures from `RJOO` and `RJBE` northwest of MAIKO. 

The published hold for missed approaches is `LILAC` +3000 for 06L, `AKASI` +4000 (via MAIKO) for 06R.

-	Landing/departing RWY 24L/24R

This is the south wind configuration for RJBB. 

Vectors onto the localizer should NOT be used. Approaches are available from `MAYAH` (24L), or `AMBER` (24L) and `BEIGE` (24R). Arrivals can be vectored over the sea west of Awaji Island if needed on top of `RJBE` arrivals.

Use care not to descend arrivals into the `RJBE` PCA. Cross `JOLLY` (from `DANDE`) +8000, `AWAJI` +7000, `MAYAH` 4000 (**at** 4000). Aircraft should descend as per the approach after MAYAH in order to main separation from `RJBE` traffic. Note that due to the lack of circle to land approaches in Endless ATC, `RJBE` 27 arrivals will fly a long downwind at \~1300 and may conflict with `RJBB` 24 arrivals leaving 2600. Having the `RJBE` arrival fly slightly ahead of an overhead `RJBB` arrival should allow for separation to be maintained.

Departures to the west will be climbing through arrivals descending to 4000 from `AWAJI` to `LILAC` to `MAYAH` and over `RJBE departures`. Departures over `DAISY` should cross `DAISY` +6000 and JULIA +8000. Departures over HELEN should cross `HELEN` +8000. Due care will need to be taken to maintain separation. Recommend descending to arrivals to 4000 after `AWAJI`, and expediting climb of departures from 24R. Departures to the west may also conflict with `RJBE` departures and `RJOO` departures to the west.

Departures to the south may conflict with arrivals from DANDE and the south/southwest. Use caution.

### `RJOO` 大阪国際空港(伊丹)

＊未翻訳
An airport near the heart of Osaka, only domestic traffic is handled aside from the odd state aircraft. Mountains surround the airport to the north, west, and east.

There is custom traffic for `RJOO`. The proportions are very much estimates but shouldn't be too far off from reality.

Aircraft arrive at:

- `ROKKO` (northwest from northwestern Japan, northeast from northeastern Japan)
- `KODAI` (east from eastern Japan)
- `KAZRA` -> `MIRIO` -> `KAINA` -> `IZUMI` (west from western Japan)
- `JANGO` -> `MIRIO` -> `KAINA` -> `IZUMI` (west from western Japan)
- `MUGIE` -> `HONMA` -> `KAINA` -> `IZUMI` (southwest from southwestern Japan)

Aircraft depart via:

- `SHTLE` (east for Tokyo)
- `MINAC` (northeast to Tohoku, Hokkaido)
- `TOZAN` (northwest to Taiwan, HK, Singapore, Malaysia, etc.)
- `SOUJA` (west to north Kyushu)
- `WASYU` (west to western Japan, central Kyushu)
- `KRE` (southwest to southwestern Japan, south Kyushu)

There are two runways:

- 14R/32L
- 14L/32R

Larger aircraft land 14R/32L, as 14L/32R is generally only suitable for aircraft A320/B738 or smaller. It is not possible to model this in the game however.

Note that simultaneous parallel independent approaches are not used at `RJOO`. It is possible in the game, but the approaches are not built with this in mind. Of course, you can still do simultaneous parallel dependent approaches with staggered sequencing, which can help with dealing with wake turbulence separation, however, this would not be used in reality as the runways are too close to each other.

Airspace to vector arrivals for sequencing is avaiable south of IKOMA/southeast of IZUMI/west of KODAI. Arrivals will fly over `RJOY` Yao, use care not to descend into YAO airspace. Use care to keep separation at `KAINA`, `ROKKO` and near `IKOMA`.

West departures may conflict with other aircraft on west departures. Use caution.

The missed approach hold is IZUMI +3000.

There are two simple runway configurations:

-	Landing and departing 32L/32R

The preferred runway configuration.

Due to the mountains surrounding the airport, departures make a climbing left turn towards the south.

-	Landing and departing 14L/14R

This runway configuration is only used when winds do not allow for use of the 32s. Arrivals circle west of the airport to land the 14s within the mountainous surroundings.

Due to the lack of circle to land approaches in Endless ATC, aircraft make long downwind to 14. Note that in real life these aircraft would have long flown into terrain, but this is the best we can do here.

Departures may conflict with arrivals circling to 14. Use caution.

West departures may conflict with other aircraft on west departures or arrivals to `RJBE`/`RJOT`/`RJOB`. Use caution.

### `RJBE` 神戸空港

＊未翻訳
A smaller airport in Osaka Bay minutes from central Kobe. Located under to approach to the 24s at `RJBB`, typically in-out operations landing 09 and departing 27 are ideal. Unfortunately, this is not possible in Endless ATC.

There is custom traffic for `RJBE`. The proportions are very much estimates but shouldn't be too far off from reality.

Aircraft arrive at:

- `GINJI` (east from eastern Japan)
- `WAKIT` (northeast from northeastern Japan)
- `RANDY` -> `BERTH` (west from western Japan)
- `KARIN` -> `BECKY` (southwest from southwestern Japan)

Aircraft depart via:

- `SHTLE` (east for Tokyo)
- `CUE` (east to eastern Japan)
- `YME` (northeast to Tohoku/Hokkaido)
- `SOUJA` (west to north Kyushu)
- `WASYU` (west to western Japan, central Kyushu)
- `POPPY` (southwest to southwestern Japan, south Kyushu)

Aircraft arriving/departing `RJBE` in general will be operating under `RJBB` traffic. Ensure that arrivals are low enough before entering the bay, and that departures are clear of traffic above before issuing further climb.

Arrivals can be vectored over the sea west of Awaji Island.

Departures may conflict with other aircraft on west departures or arrivals to `RJOT`/`RJOB`. Use caution.

The missed approach hold is SIOJI +3000.

There are two simple runway configurations:

-	Landing and departing 09

The preferred runway configuration. Departures make a climbing right turn to depart to the west remaining under `RJBB` departures and over `RJBE` arrivals.

-	Landing and departing 27

This runway configuration is used when `RJBB` is landing 24, as Endless ATC requires departures to climb to a minimum of 3000 which would conflict with the `RJBB` 24 approach path. Arrivals circle to land 27, however as Endless ATC does not have circle to land approaches, arrivals make a long downwind to 27, and may conflict with RJBB arrivals leaving 2600. Having the `RJBE` arrival fly slightly ahead of an overhead `RJBB` arrival should allow for separation to be maintained.

Departures will need to climb to 4000 or higher to clear arrivals at 3000.

### `RJOS` 徳島空港

＊未翻訳
A joint-use civilian airport and JSDF-M base. Training operations with Beech King Airs are conducted by the JSDF-M from this base. Typically in-out operations landing 29 and departing 11 are ideal; unfortunately, this is not possible in Endless ATC.

There is custom traffic for `RJOS`. The proportions are very much estimates but shouldn't be too far off from reality.

Aircraft arrive at:

- `JOSIN` (southeast to training areas?)
- `SINGU` -> ... -> `DATIS` (east from Tokyo)
- `KTE` -> `KULUL` -> `TSC` (west from Fukuoka)

Aircraft depart via:

- `KMANO` (east for Tokyo)
- `KTE` -> `WASYU` (west to Fukuoka)
- `TOSAR` (south to training areas?)

Departures may conflict with other aircraft on southwest departures and `RJBB` `CANDY` arrivals. Use caution.

The missed approach hold is TSC/DATIS +3000.

There are two simple runway configurations:

-	Landing and departing 29

The preferred runway configuration. Departures make a climbing left turn to depart to the southeast.

-	Landing and departing 11

This runway configuration is used when winds do not allow straight-in 29. Arrivals circle to land 11, however as Endless ATC does not have circle to land approaches, arrivals make a long downwind to 11.

### `RJOT` 高松空港

＊未翻訳
An airport nestled up against mountains to the south serving Takamatsu.

There is custom traffic for `RJOT`. The proportions are very much estimates but shouldn't be too far off from reality.

Aircraft arrive at:

- `GINJI` (east)
- (`TAKMA`) -> `KTE` (west/southwest)
- (`YUBAR`) -> `OYE` -> `KTE` (northwest)

Aircraft depart via:

- `SHTLE` (east)
- `WASYU` (west)
- `TAROH` (north)

The missed approach hold is KTE +5000.

There are two simple runway configurations:

-	Landing and departing 26

The preferred runway configuration.

-	Landing and departing 11

This runway configuration is used when winds do not allow straight-in 26. Arrivals circle to land 11, however as Endless ATC does not have circle to land approaches, arrivals make a long downwind to 11.

### `RJOB` 岡山空港

＊未翻訳
An airport situated in the mountains serving Okayama.

There is custom traffic for `RJOB`. The proportions are very much estimates but shouldn't be too far off from reality.

Aircraft arrive at:

- `GINJI` (east)
- `WAKIT` (northeast)
- (`YUBAR`) -> `OYE`(north)
- (`TAKMA`) -> `INOOK` (west/southwest)

Aircraft depart via:

- `SHTLE` (east)
- `YME` (northeast)
- `YUBAR` (north)
- `WASYU` (west)

The missed approach hold is `OYE`/`BENES` +4000.

There are two simple runway configurations:

-	Landing and departing 07

The preferred runway configuration for arrivals from the west. A RNAV AR approach utilizing RF legs to circle to 07 from the east is available in reality but the final leg is too short to be reproducible in Endless ATC. Therefore, east arrivals fly the ILS from OYE.

-	Landing and departing 25

The preferred runway configuration for arrivals from the east. The straight-in to 25 is an RNAV approach as there is no ILS for 25.

### `RJOY` 八尾空港

＊未翻訳
A small airport near Osaka that acts as a general aviation gateway.

There is custom traffic for `RJOY`. The proportions are very much estimates but shouldn't be too far off from reality.

Aircraft arrive at:

- (`MIDER`) -> `ITE` (east)
- `ROKKO` (north)
- (`YUBAR`) -> `OYE`(northwest)
- (`KAIFU` -> `IZARI`) -> `MIKAN` (west/southwest)
- (`NORAN`) -> `IZUMI` (southeast)

Aircraft depart via:

- `KCC` via `ASUKA` (east)
- `KRE` via `IZUMI`, `ITE`, `OLIVE` (southwest)
- `YME` via `IZUMI` (north)
- `YUBAR` via `IZUMI` (northwest)
- `WASYU` via `IZUMI` (west)

The missed approach hold is `IZUMI` +4200.

The only instrument approaches available are a VORDME or VOR circling approach from `IZUMI`. The VORDME approach is implemented with circling to all runways. Runway 13/31 is not enabled at this time, but can be easily enabled by editing [configurations] as the other relevant data is all there.

There is a very high potential for conflicts to the west of the airport. The airport and the VORDME approach sit under the approach path for `RJOO` traffic via `IZUMI`, so you effectively have a ceiling of 5000 to work with when there is traffic overhead. Alternatively, you can vector `RJOO` arrivals to the south to clear the airspace overhead.

Aircraft inbound to `IZUMI` via V55 from `ITE` will need to stay above `RJOO` departures and `RJBB` arrivals, while staying below `RJBB` `NANKO` departures, `RJOO` arrivals via `IZUMI`, and `RJOY` `ASUKA` departures. Aircraft departing via `IZUMI` (V55) `ITE` will also need to separated from opposite direction inbound traffic. Any aircraft going missed will also need to be separated from other `RJOY` arrivals, and in the case of landing 09, from aircraft inbound the `RJOO` 32s.

There are two simple runway configurations:

-	Landing and departing 27

The calm wind configuration. Use care for `ASUKA` departures; keep them separated from arrivals inbound `IZUMI` from `ITE`, and climb them above aircraft on final for `RJOO`.

-	Landing and departing 09

The reverse configuration. Use care for `ASUKA` departures to keep them separated from arrivals inbound `IZUMI` from `ITE`.

## 既知の問題点

- 旋回進入...............実装できていますが、かなりの余裕のあるベースターンとファイナルアプローチじゃないとミスアプローチのなるので結構広い旋回進入となっています。

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
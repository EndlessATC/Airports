# `RJTT` 進入管制区 3.3.0

＊作者は日本人ではないため、圧倒的語彙力のなさと知識不足によるおかしいまたは間違っている表現があるかもしれません。

TOKYO ACA(東京進入管制区)を[Endless ATC](https://steamcommunity.com/app/666610)に実装する追加データファイルです。`RJTT`東京国際空港(羽田)と`RJAA`成田国際空港が再現されています. 海上自衛隊の`RJTL`下総基地も高難易度及び高スコアでは再現されています. 空域の上限はFL240です.

AIP Japan 2021/08/12　（国土交通省） （https://aisjapan.mlit.go.jp/) をもとに作成しています。再現されているSID及びSTARは現実の運用と異なる場合があるかもしれませんが、基本的に日中の景気気象状態 (IMC) を再現しているつもりです。すべての航空機がRNAV対応としていて、RNAVの代わりがない場合を除き非RNAVのSID及びSTARは実装されていません。海岸のデータはnaturalearthdata.comのを使っています。

TOKYO ACAは日本最大の二つの空港を含む非常に広い空域です。羽田と成田に飛来する航空機の数が膨大ではありますが、これら二つの空港で定められたSID及びSTARはよく作られていて、それによって大量の航空機を捌けることができます。 プレイヤーの仕事は到着機感覚の整理と合流ポイントの監視がほとんどで、STAR外の遅延ベクターなしで40以上のスコアを叩き出せるはずです。

STARはこのゲームの進入方式で再現されています。進入方式に従って飛行することをを許可できる飛行機は有効なポイントに向かっていなければなりません。友好のポイントにDCTの指示を出した後、ILSの指示の代わりにAPP指示を出せます。一つのポイントから複数の進入方式が始まる場合もあります。指示を確定する前にまたAPPのボタンをクリック/キーを押すと次の進入方式に変わります。選択している飛行機がすでに進入方式に従って飛行しているならば、いったんDCTでポイントに向かう指示を選択しなければ飛行方式の変更はできません。

ヘリはゲームに実装されていませんので、海上自衛隊の`RJTE`館山基地と陸上自衛隊の`RJTK`木更津駐屯地`RJAK`霞ヶ浦駐屯地は実装されていません。
`RJTY`横田進入管制区にある `RJTF` 調布飛行場からの小型飛行機、またはヘリしか飛んでこない`RJTO`大島空港と`RJAN`新島空港も実装されていません。東京進入管制区の一部の下は横田進入管制区の空域ですが、ゲームの仕様上これも管制空域に入っています（しかし入ってはいけないエリアとなっています）。そのため飛行機はその横田の空域に出ていくことも、その空域から来るのも再現するのはが難しいです。ただし、`RJTO`、`RJAN`、`RJTF`滑走路はマップ上に示しています。

## 登場する空港

### `RJTT` 東京（羽田）国際空港

羽田空港です。国内便が多いですが、国際便もあります。出発便は西へのが多くて、到着便は南西方向から多く飛来します。

発着便の設定は推測ですが現実とかけ離れてることはないでしょう。

マップ上のフィックスのいくつかは指定のホールドが設定されています。ミスドアプローチのホールドは34L/23/16Rなら`UTIBO`、34R/22なら`KASGA`, 16Lなら`SNOKE`.

＊未翻訳
Aircraft arrive at 6 points:

- `SPENS` -`Y71`-> `XAC` (west from western Japan, Korea, Northern China)
- `SELNO` -`Y21`-> `RUNSO` -`Y21`-> `AKSEL` (south west from southwestern Japan, Okinawa, Southeast Asia)
- `TOPIT` -`Y875`-> `RURER` -`Y875`-> `AROSA` (south from Hachijojima, Indonesia/Australia)
- `DOLBA` -`Y824`-> `AROSA` (southeast from oceanic, Australia/NZ/Pacific islands, Guam)
- `TEDIX` -`Y10`-> `GODIN` (north from northern Japan, Russia, Europe, east NA)
- `LALID` -`Y807`-> `POLIX` (east from oceanic, west NA/SA, Hawaii)

Aircraft depart via:

- `CLARK` (northnorthwest for Russia/Europe)
- `AGRIS` (north for northern Japan and beyond)
- `GULBO` (northeastern oceanic)
- `BORLO` (east oceanic)
- `ANSAD` (southeastern oceanic)
- `NURLI` (south)
- `KAGNA` (southwest and Osaka)
- `NINOX` (west for southern western Japan and beyond)
- `RITLA` (west for central western Japan and beyond)
- `BEKLA` (northwest such as Korea/north China/north side of western Japan)

(`VAMOS` departures to `UTIBO` aren't implemented as there are no standard flight planned routes from `RJTT` that use this transition.)

There are four runways:

- 16R/34L (RWY A) 
- 04/22 (RWY B)
- 16L/34R (RWY C)
- 05/23 (RWY D)

A few different configurations are used in real operations; four are available in this version of `RJTT` ACA:

-	Landing 34L/34R, departing 34R/05
	
	In general, arrivals from the southwest (`XAC`, `AKSEL`, `AROSA`) land 34L and arrivals from the northeast (`GODIN`, `POLIX`) land 34R. Departures to the northeast takeoff from 34R, and departures to the southwest takeoff from 05 in general.

	34L handles the higher amounts of traffic from the southwest, and 05 handles the higher amounts of traffic heading southwest. The lower amounts of traffic to/from the northeast share 34R in mixed operation. 04 is not used in this configuration as it conflicts with landings on 34L (in real life, it may be used for some GA departures?).

	Approaches to 34L (RWY *A*) and 34R (RWY *C*) are available using APP mode from *A*RLON and *C*REAM respectively, with transitions from `ARLON` or `CAMEL` depending whether the aircraft is approaching from the south or the east.

	STARs are available using APP mode from `XAC`, `RUNSO`, `AROSA`, `GODIN`, `MILIT`, and many other intermediate points on the STARs. `STARS` to 34L/34R implement a point merge system around `WEDGE` for 34L and `CREAM` for 34R. Aircraft fly an arc around a point (`WEDGE`/`CREAM`), and you can sequence planes by directing planes to proceed direct `WEDGE`/`CREAM` and activate APP mode. By default south arrivals fly STARs and approaches to 34L, but you can engage APP mode twice to have planes swing wide of the `WEDGE` arc to join the `CREAM` arc for 34R.

	Note that higher arrivals will conflict with lower arrivals when descending from the point merge arc to meet the =8000 restriction at `WEDGE`. Either descend the lower arrival (watch out for further lower arrivals) or prioritize the lower arrival over the higher arrival. Also watch for `AROSA` arrivals conflicting with arrivals to `RJAA`.

	Note that the normal runway operation for 34L/34R arrivals (`HIGHW`AY `VISUA`L 34R and ILS X 34L from `KAIHO`) is not possible to implement due to the lack of visual approaches in the game and the fact that aircraft joining the parallel ILS above `RJTK` Kisarazu would conflict as they are at the same altitude. Therefore the approaches depicted are illustrative of IMC conditions necessitating the use of parallel ILS approaches.

	For an extra challenge, try routing ANA/SNJ/ADO/VIP flights to 34R (T2/VIP area) and JAL/SFJ/SKY/international/GA flights to 34L (T1/T3/N area).

-	Landing 22/23 (ILS), departing 16L/16R
	
	In general, arrivals from the southwest (`XAC`, `AKSEL`, `AROSA`) land **\*22\*** and arrivals from the northeast (`GODIN`, `POLIX`) land **\*23\***. Departures to the northeast takeoff from 34R, and departures to the southwest takeoff from 05 in general.

	22/16R handles the higher amounts of traffic to/from the southwest as they do not conflict with other runways (16R departures depart before the intersection with 22). As RWY23 arrivals conflict with departures from both 16s, it is used for traffic arriving from the northeast.

	Approaches to 22 and 23 are available using APP mode from `NEXUS` and `SMILE` respectively, with transitions from *N*YLON or *S*TEAM depending whether the aircraft is approaching from the *n*orth or the *s*outh.

	`STARS` are available using APP mode from `XAC`, `RUNSO`, `AROSA`, `GODIN`, `MILIT`, and many other intermediate points on the STARs. STARs from the southwest implement a point merge system around `SHAFT` (STARs from the northeast are traditional). Aircraft fly an arc around a `SHAFT`, and you can sequence planes by directing planes to proceed direct `SHAFT` and activate APP mode. By default south arrivals fly STARs and approaches to 22, but you can engage APP mode twice to have planes descend under the `SHAFT` arc to `BACON` for 23. Be careful of conflicts with traffic from the north inbound 23.

	For an extra challenge, try routing ANA/SNJ/ADO/VIP flights to 23 (T2/VIP area) and JAL/SFJ/SKY/international/GA flights to 22 (T1/T3/N area).

-	Landing 22/23 (LDA), departing 16L/16R

	The same as the previous configuration, but instead aircraft approach 22/23 following an offset localizer on a 270 degree course over Tokyo Bay, avoiding overflight of populated areas.

	**Due to a game limitation, runways 22 and 23 are called 22C and 23C in this configuration.**

	Approaches to 22 (RWY *B*) and 23 (RWY *D*) are available using APP mode from *B*ONUS and *D*OYLE respectively, with transitions from *B*ACON or *D*ATUM depending whether the aircraft is approaching from the north or the south.

	`STARS` are available using APP mode from `XAC`, `RUNSO`, `AROSA`, `GODIN`, `MILIT`, and many other intermediate points on the STARs. STARs from the southwest implement a point merge system around `SHAFT` (STARs from the northeast are traditional). Aircraft fly an arc around a `SHAFT`, and you can sequence planes by directing planes to proceed direct `SHAFT` and activate APP mode.  By default south arrivals fly STARs and approaches to 22, but you can engage APP mode twice to have planes descend under the `SHAFT` arc to `BACON` for 23. Be careful of conflicts with traffic from the north inbound 23.

	Note that the LDA approaches are represented by a runway located where one would be if the LDA approaches were straight-in ILS approaches; this is the best implementation given limitations of the game, but from an approach control perspective it should be a fairly accurate representation.

	For an extra challenge, try routing ANA/SNJ/ADO/VIP flights to 23 (T2/VIP area) and JAL/SFJ/SKY/international/GA flights to 22 (T1/T3/N area).

-	Landing 16L/16R, departing 16R/04/16L

	A new approach path flying over central Tokyo only applied in the afternoon hours, which was recently developed in response to growing traffic at `RJTT`. Normally arrivals fly close parallel RNAV tracks to the final approach course with a 3.45 degree glideslope, however, game limitations mean that parallel arrivals would be conflicting with each other all the way to the final approach fix. Therefore, the "backup" ILS approaches that take a dive into the Yokota ACA have been implemented here.

	Approaches to 16L and 16R are available using APP mode from `SANDY` and `NATTY` respectively.

	`STARS` are available using APP mode from `XAC`, `RUNSO`, `AROSA`, `GODIN`, `MILIT`, and many other intermediate points on the STARs. `STARS` to 16L/16R implement a point merge system around `SHAFT` for 16L and `NEURO` for 16R. Aircraft fly an arc around a point (`SHAFT`/`NEURO`), and you can sequence planes by directing planes to proceed direct `SHAFT`/`NEURO` and activate APP mode. By default south arrivals fly STARs and approaches to 16L, but you can engage APP mode twice to have planes fly over the `SHAFT` arc to join the `NEURO` arc for 16R.

	Note that the LDA approaches are represented by a runway located where one would be if the LDA approaches were straight-in ILS approaches; this is the best implementation given limitations of the game, but from an approach control perspective it should be a fairly accurate representation.

	For an extra challenge, try routing ANA/SNJ/ADO/VIP flights to 23 (T2/VIP area) and JAL/SFJ/SKY/international/GA flights to 22 (T1/T3/N area).

### `RJAA` 成田国際空港

成田空港です。国内便が少ないですが、LCCと国際便とカーゴ便が多いです。

発着便の設定は推測ですが現実とかけ離れてることはないでしょう。

マップ上のフィックスのいくつかは指定のホールドが設定されています。ミスドアプローチのホールドは16R/34Lなら`BINKS`で16L/34Rなら`BOSPA`.

＊未翻訳
Aircraft arrive at 4 points:

- `MOE` -`Y81`-> `BAFFY` -`Y81`-> `RUTAS` (southwest from western and southwestern)
- `TOPIT` -`Y87`-> `BAFFY` -`Y81`-> `RUTAS` (south)
- `VAGLA` -`Y813`-> `LUBLA` (northeast oceanic)
- `LESPO` -`Y809`-> `SUPOK` (southeast oceanic)
- `GURIR` -`Y30`-> `SWAMP` (north from north, northwest and northeast)

Aircraft depart via:

- `AGRIS` (northwest via `TETRA8` departure `AGRIS` transition to `Y37`)
- `KIMIN` (north via `TETRA8` departure `KIMIN` transition to `Y117`)
- `GULBO` (northeast oceanic via `GULBO2` departure to `Y808`)
- `BORLO` (east oceanic via `BORLO2` departure to `Y830`)
- `IRNOK` (southsoutheast oceanic via `OLVAN2` departure to `Y823`)
- `NORIS` (south oceanic via `OLVAN2` departure `SAMUS` transition to `Y84`)
- `SEDRI` (southwest via `PIGOK2` departure to `Y50`)
- `MITOP` (west via `REDEK2` departure to `Y60`)
- `TEPEX` (northwest via `TETRA8` departure `ENPAR` transition to `Y16`)

There are two runways:

- 16R/34L (RWY A) 
- 16L/34R (RWY B)

There are two simple runway configurations:

-	Landing and departing 34L/34R

	Approaches to 34L and 34R are available using APP mode from `GIINA` and `TEMIS` respectively, with transitions from `TYLER` or `ELGAR` depending whether the aircraft is approaching from the south or the east.

	`STARS` are available using APP mode from `BAFFY`, `SWAMP`, `SUPOK`, `LUBLA`, and many other intermediate points on the STARs. STARs to 34L implement a point merge system around `PEAKS`. Aircraft fly an arc around `PEAKS`, and you can sequence planes by directing planes to proceed direct `PEAKS` and activate APP mode. Alternate STARs are available to 34R which do not implement a point merge arc; watch out for potential conflicts with arrivals on STARs to 34L.

	Note that higher altitude arrivals on the arc will conflict with lower altitude arrivals descending from the point merge arc to meet the =6000 restriction at `PEAKS`. Either descend the lower altitude arrival (watch out for even lower altitude arrivals) or prioritize the lower altitude arrival over the higher altitude arrival.

	For arrivals from `RUTAS`, watch out for conflicts with `AROSA` arrivals to `RJTT`.

	Departures are executed in parallel and maintain horizontal separation until east of `RJAA`. Recommend not assigning higher than 7000 to 34L departures until clear of `RJTT` arrivals from `GODIN`/`POLIX`.

	For an extra challenge, try routing oneworld/LCC flights to 34R (T2/T3) and other flights to 34L (T1/cargo area).

-	Landing and departing 16L/16R

	Approaches to 16L and 16R are available using APP mode from `MARCH` and `ACELA` respectively, with transitions from `TYLER` or `ELGAR` depending whether the aircraft is approaching from the south or the east.

	`STARS` are available using APP mode from `BAFFY`, `SWAMP`, `SUPOK`, `LUBLA`, and many other intermediate points on the STARs. `STARS` to 16R implement a point merge system around `CASIO`. Aircraft fly an arc around `CASIO`, and you can sequence planes by directing planes to proceed direct `CASIO` and activate APP mode.  Alternate STARs are available to 16L which do not implement a point merge arc; watch out for potential conflicts with arrivals on STARs to 16R.

	Note that higher altitude arrivals on the arc will conflict with lower altitude arrivals descending from the point merge arc to meet the =6000 restriction at `CASIO`. Either descend the lower altitude arrival (watch out for even lower altitude arrivals) or prioritize the lower altitude arrival over the higher altitude arrival.

	Use care not to descend arrivals into `RJAH`/`RJAK` airspace.

	For an extra challenge, try routing oneworld/LCC flights to 16L (T2/T3) and other flights to 16R (T1/cargo area).

### `RJTL` 下総基地

＊未翻訳
This JSDF-M base is located under the ILS to runway 22/23 at `RJTT`. There is one runway 01/19, with an ILS approach to RWY 19 only. Use care to maintain separation of traffic from `RJTT` arrivals. When landing RWY 01, aircraft will fly the ILS 19 and circle to land RWY 01. Due to the complexity of the airspace, in Endless ATC this airport is set to open when score > 20, to allow for beginning players to understand the `RJTT` and `RJAA` routes first.

Aircraft arrive at 4 points:

- `XAC` (southwest)
- `KAMOG` (southeast)
- `KIDOR` (north)
- `LEMUM` (northwest)

Aircraft depart via:

- `DALMA` via `OMIYA`, `EDARR`, `KOSKA` (southwest)
- `KAMOG` via `TSUGA`, `OJT` (southeast)
- `OMIYA` (northwest)
- `JD` (north)

Approaches are available using APP mode from `TOHNE` and `ASEKI`. Arrival routes are available using APP mode from `XAC`, `KAMOG`, `LEMUM`, and `KIDOR`, as well as any intermediate points.

## 既知の問題点

- `RJTT`のLDAアプローチはLDAによる進入のあと目視で滑走路に降りるのではなくて、ただLDAコースと同じコースのILSアプローチを持つ現実に存在しない滑走路を配置しただけ。
- `RJTT`のRNAV　16アプローチは実装されていません。同時進入の飛行機の間隔はILSと違って高低差はないのでゲームの仕様上コンフリクトとなってペナルティを受けます。
- 晴天時の34L/34R進入方式は実装されていません(HIGHWAY VISUAL 34Rのビジュアルアプローチはゲーム上表現できないので、ゲームの仕様上ただのILSアプローチになって、`KAIHO`から合流する34L到着機とのコンフリクトになります。)
- `RJTO`大島/`RJAN`新島がない (横田からの到着を表現できない)
- 飛行機が管制空域を出る場所または管制空域に入る場所が現実と異なることがある（例えば、香港のLCCの飛行機が太平洋方面から飛んでくる)
- 南から`RJTT`の16L/16Rに着陸する飛行機がSTARで滑走路を目指してもゲームの仕様によって「遅刻」状態になりやすい（ただ飛行距離が長すぎるだけ？)

## Disclaimer

**現実と異なる点が多数あると思います（特に下総の飛行ルートはほぼ推測でしかない)**

## For Developers

この追加ファイルに貢献したい方はsource/RJTT.txtを変更してから/tools/で"deploy.py RJTT"を実行してください。

## 変更履歴

*	2.2.0 - 2020/12/02
	-日本語初リリース
*	2.2.1 - 2020/12/19
	-管制区の離脱ポイントの交通量バランスを調整しました
*	2.2.2 - 2020/12/29
	-RJTTにJCGがスポーンしない不具合を修正
*	3.0.0 - 2021/02/20
	- ソースをほぼ丸ごと再作成
	- `KC2`のWTCを修正
	- `HKE` 北総 VORDME 廃止
		- `SWIMY`、`ABBOT`廃止
		- 新たに`BOSPA`を設定
		- `TEMIS`でのホールド変更
	- READMEに出典の記載を追加
	- レア発着機を追加
	- 磁気変動を-8（2020）に更新
	- いくつのSTARの最初ポイントでの推定方向を修正（プレイへの影響はありません)
	- アークのキャパシティオーバー時のベクタリングを容易にするためにポイントマージのアークの最終ポイントからのアプローチを追加
	- FAFからのアプローチを追加、これによって直接IFからの進入が可能
	- ポイントマージアークの描写を改良
	- SIDの名前の形式を変更
		- 間違ってる名前と発音の修正
	- `RJTT` 16L/Rの優先度を修正 (16Lを優先)
	- 16Rからの離陸を22との交差点より先から始まるように修正
	- `RJTL`の発着レートを三分の一に下げました.
	- `RJAA`　ILS Y 16L/16R アプローチを実装
	- `RJTT`　ILS X 34L/ILS Y 34R アプローチを実装
*	3.1.0 - 2021/05/31
	- `TEMIS`の設定を修正　※プレイに影響はありません
	- `RJTT`のILS Z 34Lを修正
		- `ARLON`の高度5000以下の制限を解除
		- 滑走路から15.5nmiの時点(D15.7`IHA`/`APOLO`0.6nmi前)でローカライザーに合流
			- 以前は`ARLON`で合流
		- 実際`ARLON`では高度制限はなかった（正しくは`CREAM`には高度5000以上の制限があった)
	- `RJTL`の滑走路の位置情報を修正　※プレイに影響はありません
	- 各空港のタワー周波数を実装
*	3.2.0 - 2021/07/06
	- 出発機のハンドオフ先のコールサイン及び周波数を実装
	- レア発着機の追加や修正
*	3.3.0 - 2021/07/18
	- 進入管制区の各入口の維持高度を個別に設定
	- 各SIDの初期維持高度を個別に設定
	- 進入管制区の入口ポイントを進入管制区境界にあるポイントに変更
	- 到着機はSTARの飛行が許可された状態でスポーンする
		- この仕様はゲームの4.5.1のリリースまでの一時的処置
		- 後で仕様をSTARの開始点までの許可に変更する(そこでホールドに入る)
		- STARへの許可はアプローチ管制(あなた)の責任になる
	- `RJAA`の`TETRA`SIDの発音を修正
	- 一部の飛行機(`B772`など)がGSを超えてしまうのを防止するために`RJTT`ILS Z 34Lに`ARLON`での200kt制限を設ける
	- `RJTK`木更津と`RJTE`館山の滑走路を実装(オープンはしない)
		- `KZT`木更津と`TET`館山TACANを実装
	- ANA`B737`引退
	- 一部のレア発着機をユニークに(同じのは同時に2以上出現しない)
*	3.4.0 - 4.5.1リリース待ち
	- 到着機は進入管制区に入った後、RNAV経路に沿ってSTAR開始点まで飛行してホールドに入る
		- STARの許可を出すのはアプローチ管制(あなた)になる
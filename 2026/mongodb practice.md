# MongoDB 資料庫的基本操作
以看劇App為例，假設我們有一個名為 test_tv 的資料庫，其中包含一個名為 dramas 的集合，用於存儲電視劇的信息。

1. Create Database

```sql
// mongod command line
use test_tv

// VS Code Mongodb Playground
use('test_tv');
```

2. Create Collection

```sql
db.createCollection("dramas");
```

3. Insert Many Data: 戲劇資料

```sql
db.dramas.insertMany([
  {
    "name": "犯罪都市3：無法無天",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link1.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link2.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2024-06-02 00:00:00",
    "description": "第三部《犯罪都市》系列，主要講述了“野獸警察”馬錫道對抗財閥繼承人和日本黑幫老大的故事。",
    "poster": "http://poster1.jpg",
    "category": "亞洲"
  },
  {
    "name": "夢想",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link3.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link4.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2024-09-29 00:00:00",
    "description": "一部體育喜劇，講述了一群經驗不足的球員目標參加無家者世界杯的故事。",
    "poster": "http://poster2.jpg",
    "category": "亞洲"
  },
  {
    "name": "芭蕾舞者",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link5.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link6.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2023-10-15 00:00:00",
    "description": "一部復仇題材的動作驚悚片，由全鐘瑞和金智勳主演。",
    "poster": "http://poster3.jpg",
    "category": "亞洲"
  },
  {
    "name": "尚氣與十環傳奇",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link7.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link8.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2021-09-03 00:00:00",
    "description": "漫威超級英雄電影，講述了劉思慕飾演的尚氣的故事。",
    "poster": "http://poster4.jpg",
    "category": "亞洲"
  },
  {
    "name": "寄生蟲",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link9.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link10.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2019-11-07 00:00:00",
    "description": "奉俊昊執導的備受讚譽的韓國電影，講述了金氏家族的故事。",
    "poster": "http://poster5.jpg",
    "category": "得獎影片"
  },
  {
    "name": "賽博朋克：邊緣行者",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link11.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link12.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2023-09-13 00:00:00",
    "description": "一部獲得年度動畫獎的動畫系列。",
    "poster": "http://poster6.jpg",
    "category": "動漫"
  },
  {
    "name": "鬼滅之刃：遊郭篇",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link13.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link14.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2023-02-13 00:00:00",
    "description": "一部獲得最佳動作和最佳動畫獎的動畫系列。",
    "poster": "http://poster7.jpg",
    "category": "動漫"
  },
  {
    "name": "偶然與想像",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link15.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link16.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2021-12-17 00:00:00",
    "description": "濱口龍介執導的日本劇情片。",
    "poster": "http://poster8.jpg",
    "category": "國際"
  },
  {
    "name": "你傷我的感覺",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link17.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link18.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2023-02-24 00:00:00",
    "description": "一部關於小說家婚姻破裂的喜劇電影。",
    "poster": "http://poster9.jpg",
    "category": "喜劇"
  },
  {
    "name": "五月十二月",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link19.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link20.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2023-03-15 00:00:00",
    "description": "一部由娜塔莉·波特曼和朱莉安·摩爾主演的喜劇電影。",
    "poster": "http://poster10.jpg",
    "category": "喜劇"
  },
  {
    "name": "葬送的芙利蓮",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link21.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link22.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2023-01-01 00:00:00",
    "description": "一部奇幻冒險動畫，講述了芙利蓮的故事。",
    "poster": "http://poster11.jpg",
    "category": "動漫"
  },
  {
    "name": "肌肉魔法使",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link23.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link24.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2023-01-01 00:00:00",
    "description": "一部融合了魔法和健身的動畫，講述了一名肌肉魔法使的故事。",
    "poster": "http://poster12.jpg",
    "category": "動漫"
  },
  {
    "name": "藥師少女的獨語",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link25.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link26.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2023-01-01 00:00:00",
    "description": "一部關於一名藥師少女的日常生活的動畫。",
    "poster": "http://poster13.jpg",
    "category": "動漫"
  },
  {
    "name": "淚之女王",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link27.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link28.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2023-01-01 00:00:00",
    "description": "一部動人的劇情動畫，講述了淚之女王的故事。",
    "poster": "http://poster14.jpg",
    "category": "動漫"
  },
  {
    "name": "我的鬼女孩",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link29.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link30.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2024-05-25 00:00:00",
    "description": "一部關於一名男孩和他的鬼女友的動畫。",
    "poster": "http://poster15.jpg",
    "category": "動漫"
  },
  {
    "name": "非常律師禹英禑",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link31.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link32.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2022-06-29 00:00:00",
    "description": "講述了一位具有自閉症譜系障礙的天才律師禹英禑的故事。",
    "poster": "http://poster16.jpg",
    "category": "亞洲"
  },
  {
    "name": "小女子",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link33.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link34.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2022-09-03 00:00:00",
    "description": "講述了三個貧困的姐妹在一樁陰謀中奮鬥求生的故事。",
    "poster": "http://poster17.jpg",
    "category": "亞洲"
  },
  {
    "name": "二十五，二十一",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link35.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link36.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2022-02-12 00:00:00",
    "description": "講述了一段跨越歲月的愛情故事，從1998年到2001年。",
    "poster": "http://poster18.jpg",
    "category": "亞洲"
  },
  {
    "name": "黑道律師文森佐",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link37.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link38.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2021-02-20 00:00:00",
    "description": "講述了一位黑手黨律師回到韓國後，如何用黑道手段伸張正義的故事。",
    "poster": "http://poster19.jpg",
    "category": "亞洲"
  },
  {
    "name": "海岸村恰恰恰",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link39.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link40.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2021-08-28 00:00:00",
    "description": "講述了一位牙醫和一位多才多藝的村民在一個小漁村相遇並相愛的故事。",
    "poster": "http://poster20.jpg",
    "category": "亞洲"
  },
  {
    "name": "與神同行",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link41.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link42.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2017-12-20 00:00:00",
    "description": "講述了一名消防員在死後的49天內，接受神明的審判，決定他來世命運的故事。",
    "poster": "http://poster21.jpg",
    "category": "電影"
  },
  {
    "name": "燃燒",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link43.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link44.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2018-05-17 00:00:00",
    "description": "講述了一名快遞員、他的朋友以及一位神秘富豪之間的錯綜複雜的關係。",
    "poster": "http://poster22.jpg",
    "category": "電影"
  },
  {
    "name": "寄生上流",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link45.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link46.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2019-05-30 00:00:00",
    "description": "奉俊昊執導的備受讚譽的韓國電影，講述了金氏家族的故事。",
    "poster": "http://poster23.jpg",
    "category": "電影"
  },
  {
    "name": "出租車司機",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link47.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link48.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2017-08-02 00:00:00",
    "description": "改編自真實事件，講述了一位出租車司機與一名德國記者一起報導光州事件的故事。",
    "poster": "http://poster24.jpg",
    "category": "電影"
  },
  {
    "name": "薩滿",
    "episodes": [
      {
        "season": 1,
        "episode": 1,
        "link": "http://link49.com",
        "description": "第1集簡介"
      },
      {
        "season": 1,
        "episode": 2,
        "link": "http://link50.com",
        "description": "第2集簡介"
      }
    ],
    "end_date": "2024-12-30 00:00:00",
    "release_date": "2021-07-14 00:00:00",
    "description": "一部恐怖驚悚電影，講述了一個偏遠村莊中，因巫術引發的連環殺人事件。",
    "poster": "http://poster25.jpg",
    "category": "電影"
  }
]);
```

4. 查詢 分類：動漫

```sql
db.dramas.find({ category: "動漫" });
```

5. 要查詢「即將上映」的片單，可以使用 MongoDB 的比較運算子，例如 $gte（大於或等於）來查詢 release_date 大於或等於當前日期的記錄。以下是 MongoDB 查詢語法的範例：

```sql
// 假設當前日期是 2024-05-24
db.dramas.find({release_date: { $gte: "2024-05-24 00:00:00" }})
```

## 多文檔更新練習：為劇集添加 top10 標籤

1. 為劇集添加 top10 標籤
查詢條件 { name: { $in: ["淚之女王", "葬送的芙利蓮", "出租車司機", "肌肉魔法使"] } }：查找名稱符合這些條件的所有文檔。
更新操作 { $set: { tag: ["top10"] } }：將符合條件的文檔的 tag 欄位設置為 ["top10"]。

```sql
db.dramas.updateMany(
  { name: { $in: ["淚之女王", "葬送的芙利蓮", "出租車司機", "肌肉魔法使"] } },
  { $set: { tag: ["top10"] } }
)
```

2. 查詢標記為 top10 的戲劇，可以使用 MongoDB 的 find 方法來查詢包含 tag: ["top10"] 的文檔。

```sql 
db.dramas.find({tag: ["top10"]})
```

## 資料建模與操作：我的口袋名單

1. 建立 Collection: users
```sql
// 建立 Collection (MongoDB 無需顯式建立 Collection，插入資料時會自動建立)
db.createCollection("users")
```

2. 新增 users information ( 至少兩個 user )
account, password, name, followedDramas

```sql
// 插入兩個 user 資訊
db.users.insertMany([
  {
    account: "user1",
    password: "password123",
    name: "Alice",
    followedDramas: []
  },
  {
    account: "user2",
    password: "password456",
    name: "Bob",
    followedDramas: []
  }
])
```

3. 更新 users 的追蹤片單 followedDramas

```sql
// 更新 user1 的追蹤片單
db.users.updateOne(
  { account: "user1" },
  { $set: { followedDramas: ["淚之女王", "葬送的芙利蓮"] } }
)

// 更新 user2 的追蹤片單
db.users.updateOne(
  { account: "user2" },
  { $set: { followedDramas: ["出租車司機", "肌肉魔法使"] } }
)
```

4. 查詢 user 的片單資訊, 只列出 followedDramas
tips: find methods and specific projection

```sql
// 查詢所有用戶的追蹤片單，只顯示 followedDramas 欄位
db.users.find(
  {},
  { _id: 0, followedDramas: 1 }
)
```

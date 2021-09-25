use `user_registration_form_python`

LOAD DATA LOCAL INFILE './sql/ken_all.csv'
INTO TABLE zip_addresses
FIELDS
  TERMINATED BY ','
  OPTIONALLY ENCLOSED BY '"'
LINES
  TERMINATED BY '\r\n'
IGNORE 0 LINES
  (@field1, @field2, @field3, @field4, @field5, @field6, @field7, @field8, @field9)
SET
  zip_code = @field3,
  prefecture_id =
    CASE
      WHEN @field7 = '北海道' THEN 1
      WHEN @field7 = '青森県' THEN 2
      WHEN @field7 = '岩手県' THEN 3
      WHEN @field7 = '宮城県' THEN 4
      WHEN @field7 = '秋田県' THEN 5
      WHEN @field7 = '山形県' THEN 6
      WHEN @field7 = '福島県' THEN 7
      WHEN @field7 = '茨城県' THEN 8
      WHEN @field7 = '栃木県' THEN 9
      WHEN @field7 = '群馬県' THEN 10
      WHEN @field7 = '埼玉県' THEN 11
      WHEN @field7 = '千葉県' THEN 12
      WHEN @field7 = '東京都' THEN 13
      WHEN @field7 = '神奈川県' THEN 14
      WHEN @field7 = '新潟県' THEN 15
      WHEN @field7 = '富山県' THEN 16
      WHEN @field7 = '石川県' THEN 17
      WHEN @field7 = '福井県' THEN 18
      WHEN @field7 = '山梨県' THEN 19
      WHEN @field7 = '長野県' THEN 20
      WHEN @field7 = '岐阜県' THEN 21
      WHEN @field7 = '静岡県' THEN 22
      WHEN @field7 = '愛知県' THEN 23
      WHEN @field7 = '三重県' THEN 24
      WHEN @field7 = '滋賀県' THEN 25
      WHEN @field7 = '京都府' THEN 26
      WHEN @field7 = '大阪府' THEN 27
      WHEN @field7 = '兵庫県' THEN 28
      WHEN @field7 = '奈良県' THEN 29
      WHEN @field7 = '和歌山県' THEN 30
      WHEN @field7 = '鳥取県' THEN 31
      WHEN @field7 = '島根県' THEN 32
      WHEN @field7 = '岡山県' THEN 33
      WHEN @field7 = '広島県' THEN 34
      WHEN @field7 = '山口県' THEN 35
      WHEN @field7 = '徳島県' THEN 36
      WHEN @field7 = '香川県' THEN 37
      WHEN @field7 = '愛媛県' THEN 38
      WHEN @field7 = '高知県' THEN 39
      WHEN @field7 = '福岡県' THEN 40
      WHEN @field7 = '佐賀県' THEN 41
      WHEN @field7 = '長崎県' THEN 42
      WHEN @field7 = '熊本県' THEN 43
      WHEN @field7 = '大分県' THEN 44
      WHEN @field7 = '宮崎県' THEN 45
      WHEN @field7 = '鹿児島県' THEN 46
      WHEN @field7 = '沖縄県' THEN 47
      ELSE NULL
    END,
  city_district_county = trim(@field8),
  town_village_address = CASE right(@field3, 2) WHEN '00' THEN '' ELSE trim(@field9) END,
  created_at = CURRENT_TIMESTAMP(),
  updated_at = CURRENT_TIMESTAMP();

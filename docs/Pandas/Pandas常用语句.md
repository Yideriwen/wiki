## Pandas 常用语句

| **作用**                                                | **语句**                                                     | **说明**                                  |
| :------------------------------------------------------ | :----------------------------------------------------------- | :---------------------------------------- |
| 显示列名                                                | .columns                                                     |                                           |
| 显示行、列数                                            | .shape                                                       |                                           |
| 显示列数据属性                                          | .dtypes                                                      |                                           |
| 对每一列数据进行统计，包括计数，均值，std，各个分位数等 | .describe()                                                  |                                           |
| 统计空值                                                | .isna().sum()                                                |                                           |
| 统计某一列x中各个值出现的次数                           | 列.value_counts()                                            |                                           |
| 按某列排序                                              | .sort_values(列名,ascending=True)                            | ascending=True升序排列                    |
| 禁用科学计数法                                          | pd.set_option('display.float_format',lambda x : '%.2f' % x)  |                                           |
| 删除某几列                                              | .drop(axis=1, columns=[列1, 列2])                            |                                           |
| 有哪些值不同                                            | .unique()                                                    |                                           |
| 行去重                                                  | .drop_duplicates()                                           |                                           |
| 包含某字符串                                            | .str.contains('keyword', na = False)                         | na = False可以避免空值报错                |
| 是否在里面                                              | isin()                                                       |                                           |
| 创建空df                                                | df = pd.DataFrame(columns=[列名s])                           |                                           |
| 更改某列的数据类型                                      | df[[列]] = df[[列]].astype('float64')                        |                                           |
| 单列df/Series转list                                            | .tolist()                                                    |                                           |
| 组合list                                                | 1）+ 2）.extend() 3）插入 A[x:y]=B ，B插入A                  |                                           |
| 对字符串进行切片                                        | .map(lambda x: x.split("-")[0])                              | 用-分割                                   |
| list去重                                                | lst2 = list(set(lst1))                                       |                                           |
| 重置索引                                                | df.reset_index(inplace = True)                               |                                           |
| 在原df中，根据一列条件修改另一列值                      | df.loc[一列条件,另一列名] = 新值                             |                                           |
| 统计值的个数                                            | df.列名.value_counts()                                       |                                           |
| 根据列的数据类型进行筛选                                | df.select_dtype(include = ['object'])                        |                                           |
| 字符串前补0，尤其适用于月份                             | 字符串.zfill(n)                                              | n是按几位补0                              |
| 根据条件删除行                                          | df_clear = df.drop(df[df['x']<0.01].index)                   |                                           |
| 将表格中的字符串时间转换为时间格式                      | df_return_time['创建时间'] = pd.to_datetime(df_return_time['创建时间'],format = '%Y/%m/%d') | '%Y/%m/%d')，在format这里就前面的就可以了 |
| 时间差转换为数字                                        | df_return_time['时间差'] = df_return_time['时间差'].map(lambda x:x.seconds) |                                           |
| 删除某列值为空的行                                      | .dropna(subset=["age", "sex"])                               |                                           |
| 按产品名称统计设备数量                                  | df_202008[(df_202008['产品名称']=='云服务器CVM')&((df_202008['交易类型']=='包年包月新购')\|(df_202008['交易类型']=='包年包月续费'))].groupby(['子产品名称'],as_index=False)['子产品名称'].agg({'原价':'count'}) | 主要用groupby                             |
| 更换列名                                                | df.columns = ['资源ID','支付订单号','购买数量','总金额','现金','分成','赠送金','代金券','实际要退总金额','实际要退现金','实际要退分成','实际要退赠送金','实际要退代金券','使用时间比例','使用时长','开始使用时间','结束使用时间'] | 按列呈现出来                              |
| 显示全部行内容                                          | pd.set_option('display.max_rows', None)                      |                                           |
| 显示全部列内容                                          | pd.set_option('display.max_columns', None)                   |                                           |
| nan替换为0                                              | df = df.fillna(0)                                            | 空值替换为0                               |
|对比列的内容不同|列Series化，s1 = df.列1; s2 = df.列2; cdiff = s1.compare(s2)||
|对日期列进行查询/筛选|条件：列 == pd.Timestamp(\<date>)；列.date() == \<date>||
|各列求和|df_temp.loc['sum'] = df_temp.apply(lambda x:x.sum())||

* df.列名 = df['列名'] = df["列名"]
* df.loc[x,y] 中的 x，y可以为列表，用[]圈住，支持有用":"表示的范围表示
* df.dtypes显示每列的数据类型
* 条件表达式：在df.loc[x,y]中可以在x，y中写表达式，这里对列的筛选需要在x上做表达 ｜ 也可以在df.loc[x,y] [z]中的z中写表达式 ｜ 也可以df[x,y] 将表达式放在x或y
* 按值统计/分类统计：df[].value_counts()


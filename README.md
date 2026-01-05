# Neptune API Service

Simple API with Flask web framework that I use to teach some DevOps-related topics to my students.

Copyright 2021-2023 Saeid Bostandoust <ssbostan@yahoo.com>

## 接口列表

简单用户注册接口

| 方法   | 路由                  | 功能           | 状态  |
|------|---------------------|--------------|-----|
| POST | /api/v1/users       | 注册新用户        | 已实现 |
| POST | /api/v1/users/login | 用户登录获取 token | 已实现 |

countries 接口

| 方法     | 路由                   | 功能       | 状态  |
|--------|----------------------|----------|-----|
| GET    | /api/v1/countries    | 获取国家列表   | 已实现 |
| GET    | /api/v1/countries/id | 获取单个国家详情 | 已实现 |
| POST   | /api/v1/countries    | 创建新国家    | 已实现 |
| PATCH  | /api/v1/countries/id | 更新国家位置   | 已实现 |
| PUT    | /api/v1/countries/id | 更新国家信息   | 已实现 |
| DELETE | /api/v1/countries/id | 删除国家     | 已实现 |

city 接口

| 方法     | 路由                | 功能       | 状态  |
|--------|-------------------|----------|-----|
| GET    | /api/v1/cities    | 获取城市列表   | 已实现 |
| GET    | /api/v1/cities/id | 获取单个城市详情 | 已实现 |
| POST   | /api/v1/cities    | 创建新城市    | 已实现 |
| PUT    | /api/v1/cities/id | 更新城市信息   | 已实现 |
| DELETE | /api/v1/cities/id | 删除城市     | 已实现 |


- 注意：所有接口 增删改 都需要在请求头中添加 token，格式为 `Authorization: Bearer <token>`。
先 注册用户，使用用户登录获取 token，然后在后续请求中使用 token 进行身份验证。


```shell
# 注册用户
http POST  http://localhost:8080/api/v1/users username=admin password=flask

# 使用用户登录获取 token
http POST  http://localhost:8080/api/v1/login username=admin password=flask
```

使用 curl 测试 countries 接口

```sh
# 创建新国家,会报 Authorization Header，需要在请求头中添加 token
curl -X POST http://localhost:8080/api/v1/countries \
    -H "Content-Type: application/json" \
    -d '{"code": "US","name": "United States", "capital": "Washington D.C.", "longitude": -77.0369, "latitude": 38.9072}' \
    -H "Authorization: Bearer <token>"

curl -X POST http://localhost:8080/api/v1/countries \
    -H "Content-Type: application/json" \
    -d '{"code": "CN", "name": "China", "capital": "Beijing", "longitude": 116.4074, "latitude": 39.9042}'
    -H "Authorization: Bearer <token>"


# 使用 httpie 命令创建新国家
http POST http://localhost:8080/api/v1/countries code="US" name="United States" capital="Washington D.C." longitude=-77.0369 latitude=38.9072 \
"Authorization: Bearer <token>"

http POST http://localhost:8080/api/v1/countries code="CA" name="Canada" capital="Ottawa" longitude=-75.6972 latitude=45.4215 \
"Authorization: Bearer <token>"

http POST http://localhost:8080/api/v1/countries code="CN" name="China" capital="Beijing" longitude=116.4074 latitude=39.9042 \
"Authorization: Bearer <token>"

http POST http://localhost:8080/api/v1/countries code="MX" name="Mexico" capital="Mosike" longitude=53.5074 latitude=-0.3278 \
"Authorization: Bearer <token>"
    

# 获取国家列表
curl -X GET http://localhost:8080/api/v1/countries
http GET http://localhost:8080/api/v1/countries 

## 分页查看国家列表
curl -X GET "http://localhost:8080/api/v1/countries?page=2&per_page=3"

# 获取单个国家详情
curl -X GET http://localhost:8080/api/v1/countries/4978379777a14b8d9aa0a6448d7abd22


# PATCH 更新国家位置
curl -X PATCH http://localhost:8080/api/v1/countries/268c7e67ba9745558ca77da4ebeed571 \
    -H "Content-Type: application/json" \
    -d '{"longitude": 39.9042, "latitude": 116.4074}'

# PUT 更新国家全部信息
curl -X PUT http://localhost:8080/api/v1/countries/3b180d1f9d204b8880ebd6f00e588d11 \
    -H "Content-Type: application/json" \
    -d '{"code": "US","name": "United States", "capital": "Washington-ljd", "longitude": -77.0369, "latitude": 38.9072}'

# 删除国家
curl -X DELETE http://localhost:8080/api/v1/countries/
http DELETE http://localhost:8080/api/v1/countries/c92ab0a217744026ac01f972797d95fd
```

使用 curl 测试 city 接口

```sh
# 创建新城市
curl -X POST http://localhost:8080/api/v1/cities \
    -H "Content-Type: application/json" \
    -d '{"name": "New York", "country_code": "US", "population": 8419000, "country_id": "3b180d1f9d204b8880ebd6f00e588d11"}'
    
curl -X POST http://localhost:8080/api/v1/cities \
    -H "Content-Type: application/json" \
    -d '{"name": "Toronto", "country_code": "CA", "population": 2731571, "country_id": "c021829dd449497f9224117c5808fbcb"}'
    
curl -X POST http://localhost:8080/api/v1/cities \
    -H "Content-Type: application/json" \
    -d '{"name": "shenzhen", "country_code": "CN", "population": 21516000, "country_id": "268c7e67ba9745558ca77da4ebeed571"}'
    
curl -X POST http://localhost:8080/api/v1/cities \
    -H "Content-Type: application/json" \
    -d '{"name": "Mexico City", "country_code": "MX", "population": 12657400, "country_id": "613f35542193444ab4591403146e194a"}'

    
# 获取城市列表
curl -X GET http://localhost:8080/api/v1/cities


# 获取单个城市详情
curl -X GET http://localhost:8080/api/v1/cities/1



# PUT 更新城市全部信息
curl -X PUT http://localhost:8080/api/v1/cities/1 \
    -H "Content-Type: application/json" \
    -d '{"name": "New York City", "country_code": "US"}'


# 删除城市
curl -X DELETE http://localhost:8080/api/v1/cities/4
```

from elasticsearch import Elasticsearch

# 첫 id 는 'elastic'이며 비밀번호는 처음 주어진 비밀번호(변경가능함)
ELASTIC_ID = "elastic"
ELASTIC_PASSWORD = "oABb9ggmAOW1ISl9IxSx"

# client instance 생성
client = Elasticsearch(
    "https://localhost:9200",
    ca_certs="C:/Users/main/Desktop/es8/elasticsearch/config/certs/http_ca.crt",
    basic_auth=(ELASTIC_ID, ELASTIC_PASSWORD),
)

# 접속이 잘 되었다면 아래 코드로 확인 가능함.
print(client.info())
# result = client.indices.create(index="my_index")
# print(result)

# 문서 생성
# result = client.index(
#     index="my_index2",
#     id="my_document_id",
#     document={"field1": "value1", "field2": "value2"},
# )

# print(result)

# 문서 조회하기
# result = client.get(index="my_index2", id="my_document_id")
# print(result)

# # 문서검색
# result = client.search(index="my_index2", query={"match": {"field": "value1"}})

# print(result)

# 문서 수정
result = client.update(
    index="my_index2",
    id="my_document_id",
    doc={"field1": "new value1", "new_field": "new value2"},
)

print(result)

result = client.get(index="my_index2", id="my_document_id")
print(result)


# 문서 삭제하기
result = client.delete(index="my_index2", id="my_document_id")
print(result)

result = client.get(index="my_index2", id="my_document_id")
print(result)

#!/bin/bash

# Note this tests the current implementation of the prototype back-end, and
# not necessarily the final/desired API.

echo "This will fail (not enough data)"
grpcurl -plaintext -d '{"text": "foo"}' localhost:50051 kittens.post.Posts/Create

echo "Create an OP"
OP=$(grpcurl -plaintext -d '{"text": "foo", "conversationTitle": "test"}' localhost:50051 kittens.post.Posts/Create | jq -r .id)
echo "Created OP: ${OP}"

echo "Create a reply"
REPLY=$(grpcurl -plaintext -d '{"text": "bar", "inReplyTo": "'"${OP}"'", "authorDisplayName": "Bob"}' localhost:50051 kittens.post.Posts/Create | jq -r .id)
echo "Created reply: ${REPLY}"

echo "Create a few more posts in the conversation"
REPLY2=$(grpcurl -plaintext -d '{"text": "bar", "inReplyTo": "'"${OP}"'", "authorDisplayName": "Faye"}' localhost:50051 kittens.post.Posts/Create | jq -r .id)
grpcurl -plaintext -d '{"text": "bar", "inReplyTo": "'"${REPLY}"'", "authorDisplayName": "Anonymous Coward"}' localhost:50051 kittens.post.Posts/Create
ANNE=$(grpcurl -plaintext -d '{"text": "bar", "inReplyTo": "'"${OP}"'", "authorDisplayName": "Anne Onymous"}' localhost:50051 kittens.post.Posts/Create | jq -r .created)
grpcurl -plaintext -d '{"text": "bar", "inReplyTo": "'"${REPLY2}"'", "authorDisplayName": "Anonymous Coward"}' localhost:50051 kittens.post.Posts/Create
grpcurl -plaintext -d '{"text": "bar", "inReplyTo": "'"${REPLY2}"'", "authorDisplayName": "Bob"}' localhost:50051 kittens.post.Posts/Create

echo "Get all posts by Anonymous Coward"
grpcurl -plaintext -d '{"authorId": "Anonymous Coward"}' localhost:50051 kittens.post.Posts/PostsByUser

echo "Get all posts in our conversation"
grpcurl -plaintext -d '{"postId": "'"${OP}"'"}' localhost:50051 kittens.post.Posts/Thread

echo "Get all posts in our conversation after Faye's"
grpcurl -plaintext -d '{"postId": "'"${OP}"'", "after": "'"${REPLY2}"'"}' localhost:50051 kittens.post.Posts/Thread

echo "Get all posts in our conversation since Anne's (${ANNE})"
grpcurl -plaintext -d '{"postId": "'"${OP}"'", "since": "'"${ANNE}"'"}' localhost:50051 kittens.post.Posts/Thread

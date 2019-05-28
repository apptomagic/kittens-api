#!/bin/bash
echo "This will fail (not enough data)"
grpcurl -plaintext -d '{"text": "foo"}' localhost:50051 kittens.post.Posts/Create

echo "Create an OP"
OP=$(grpcurl -plaintext -d '{"text": "foo", "conversationTitle": "test"}' localhost:50051 kittens.post.Posts/Create | jq -r .id)
echo "Created OP: ${OP}"

echo "Create a reply"
REPLY=$(grpcurl -plaintext -d '{"text": "bar", "inReplyTo": "'"${OP}"'", "authorDisplayName": "Bob"}' localhost:50051 kittens.post.Posts/Create | jq -r .id)
echo "Created reply: ${REPLY}"

echo "Get all posts by Anonymous Coward"
grpcurl -plaintext -d '{"authorId": "Anonymous Coward"}' localhost:50051 kittens.post.Posts/PostsByUser

echo "Get all posts in our new conversation"
grpcurl -plaintext -d '{"postId": "'"${OP}"'"}' localhost:50051 kittens.post.Posts/Thread

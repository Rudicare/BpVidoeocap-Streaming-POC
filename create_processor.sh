aws rekognition create-stream-processor \
  --name AvatarProcessor \
  --input '{"KinesisVideoStream":{"Arn":"arn:aws:kinesisvideo:us-east-2:777249090794:stream/AvatarUserStream/1743515747683"}}' \
  --output '{"KinesisDataStream":{"Arn":"arn:aws:kinesis:us-east-2:777249090794:stream/AmazonRekognition-AvatarResults"}}' \
  --role-arn arn:aws:iam::777249090794:role/Rekognition-Avatar-Role \
  --settings '{"FaceSearch":{"CollectionId":"none"}}'

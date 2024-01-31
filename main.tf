resource "aws_s3_bucket" "web_bucket_a" {
  bucket   = "web_bucket_a"
  acl      = "public-read"

  website {
    index_document = "index.html"
  }

  versioning {
    enabled = true
  }

  tags = {
    Name      = "web_bucket_a_tag"
    terraform = "true"
  }
}

resource "aws_s3_bucket" "web_bucket_b" {
  bucket   = "web_bucket_b"
  acl      = "public-read"

  website {
    index_document = "index.html"
  }

  versioning {
    enabled = true
  }

  tags = {
    Name      = "web_bucket_b_tag"
    terraform = "true"
  }
}

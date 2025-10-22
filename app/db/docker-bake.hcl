group "default" {
  targets = ["db"]
}

variable "DB_VERSION" {
  default = "9.1.0"
}

target "db" {
  context    = "."
  dockerfile = "Dockerfile"
  tags       = ["mysql-msgs:${DB_VERSION}"]
}

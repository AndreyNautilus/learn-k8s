group "default" {
  targets = ["backend"]
}

variable "BACKEND_VERSION" {
  default = "1.0.0"
}

target "backend" {
  context    = "."
  dockerfile = "Dockerfile"
  tags       = ["app-backend:${BACKEND_VERSION}"]
}

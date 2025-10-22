group "default" {
  targets = ["frontend"]
}

variable "FRONTEND_VERSION" {
  default = "1.0.0"
}

target "frontend" {
  context    = "."
  dockerfile = "Dockerfile"
  tags       = ["app-frontend:${FRONTEND_VERSION}"]
}

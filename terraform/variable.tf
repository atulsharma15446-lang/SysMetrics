variable "aws_region" {
  default = "ap-south-1"
 }
variable "key_name" {
  type = string
 }
variable "ubuntu_ami" {
  type = string
 }
variable "vpc_cidr" {
  default= "10.0.0.0/24"
 }
variable "db_username" {
  default= "admin"
 }
variable "db_password" {
  type= string
  sensitive= true
 }


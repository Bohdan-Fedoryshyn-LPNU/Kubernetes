variable "region" {
  #type    = "string"
  default = "eu-central-1"
}
variable "ami_id" {
 # type = "map"
  default = {
    us-east-1    = "ami-035b3c7efe6d061d5"
    us-east-2    = "ami-02ccb28830b645a41"
    #Ubuntu
    eu-central-1 = "ami-0caef02b518350c8b"
    #CentOs
    #eu-central-1 = "ami-070b208e993b59cea"
}

}
variable "instance_type" {
 # type    = "string"
  default = "m5.large"
}
#variable "key_name" {
  #type    = "string"
#  default = "id_rsa.pub"
#}

variable "cidr" {
  description = "The CIDR block for the VPC. Default value is a valid CIDR, but not acceptable by AWS and should be overridden"
  #type        = string
  default     = "10.0.0.0/16"
}
variable "instance_tenancy" {
  description = "A tenancy option for instances launched into the VPC"
 # type        = string
  default     = "default"
}

variable "enable_dns_hostnames" {
  description = "Should be true to enable DNS hostnames in the VPC"
 # type        = bool
  default     = true
}

variable "enable_dns_support" {
  description = "Should be true to enable DNS support in the VPC"
#  type        = bool
  default     = true
}

variable "enable_classiclink" {
  description = "Should be true to enable ClassicLink for the VPC. Only valid in regions and accounts that support EC2 Classic."
 # type        = bool
  default     = false
}

variable "tags" {
  description = "A map of tags to add to all resources"
  #type        = string
  default     = "Vpc-custom-demo"
}

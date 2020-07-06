# Configure the Alicloud Provider
provider "alicloud" {
  access_key = "__________________"
  secret_key = "__________________"
  region     = "eu-west-1"
}

data "alicloud_instance_types" "2c4g" {
  cpu_core_count = 1
  memory_size = 2
}

# Create a web server
resource "alicloud_instance" "web" {
  image_id          = "ubuntu_16_0402_64_20G_alibase_20180409.vhd"
  internet_charge_type  = "PayByBandwidth"

  instance_type        = "${data.alicloud_instance_types.2c4g.instance_types.0.id}"
  system_disk_category = "cloud_efficiency"
  security_groups      = ["sg-d7ohws07rbr7az8733jq"]
  instance_name        = "web"
  vswitch_id = "vsw-d7oy0qosdnpjzwu1pot6a"
 }

terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  token     = ""
  cloud_id  = "b1gioclo0tmo2u4giv3r"
  folder_id = "b1g9qk8kfl0vmmdrjtrt"
  zone      = "ru-central1-a"
}

resource "yandex_serverless_container" "test-container" {
   name               = "hello"
   memory             = 128
   service_account_id = "ajesg8uncigc1uprdehg"
   image {
       url = "cr.yandex/crpq8c63fds29h0bqsnm/node:hello"
   }
}

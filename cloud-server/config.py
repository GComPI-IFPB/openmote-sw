mqtt_config = {
    "mqtt_id": "",
    "mqtt_address": "",
    "mqtt_port": ,
    "mqtt_subscribe_topics": [""],
    "mqtt_publish_topics": [""]
}

packet_config = {
    "timeout_ms": 0,
    "all_keys": {""},
    "keep_keys": [""]
}

calibration_config = {
    "use_calibration": False
}

calibration_values = {
}

influxdb_config = {
  "influxdb_address": "",
  "influxdb_port": ,
  "influxdb_user": "",
  "influxdb_password": "",
  "influxdb_database": "",
  "influxdb_measurements":
    {
      "on_message":     {"store": True, "measurement": ""}, 
      "on_consolidate": {"store": True, "measurement": ""}
    }
}

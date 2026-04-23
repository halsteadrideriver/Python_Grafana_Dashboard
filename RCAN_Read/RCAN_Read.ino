#include "driver/twai.h"

TaskHandle_t Task1;
TaskHandle_t Task2;

twai_message_t message;

void setup() {
  Serial.begin(115200);
  //twai_general_config_t g_config = TWAI_GENERAL_CONFIG_DEFAULT(GPIO_NUM_5, GPIO_NUM_4, TWAI_MODE_NORMAL);
  twai_general_config_t g_config = TWAI_GENERAL_CONFIG_DEFAULT(GPIO_NUM_39, GPIO_NUM_38, TWAI_MODE_NORMAL);
  twai_timing_config_t t_config = TWAI_TIMING_CONFIG_500KBITS();
  twai_filter_config_t f_config = TWAI_FILTER_CONFIG_ACCEPT_ALL();
  twai_driver_install(&g_config, &t_config, &f_config);
  twai_start();
  xTaskCreatePinnedToCore(can_print, "Task1", 8192, NULL, 1, &Task1, 0);
  xTaskCreatePinnedToCore(can_read, "Task2", 8192, NULL, 1, &Task2, 1);
  delay(1000);
  Serial.println("CAN_ID,Byte_0,Byte_1,Byte_2,Byte_3,Byte_4,Byte_5,Byte_6,Byte_7");
}
void loop() {
}
//Read CAN data
void can_read(void* pvParameters) {
  while (true) {
    if (twai_receive(&message, 0) == ESP_OK) {
      message.identifier;
      message.data[0];
      message.data[1];
      message.data[2];
      message.data[3];
      message.data[4];
      message.data[5];
      message.data[6];
      message.data[7];
    }
  }
}
//CAN Print
void can_print(void* pvParameters) {
  while (true) {
    Serial.print(String(message.identifier, HEX) + "," + String(message.data[0], HEX) + "," + String(message.data[1], HEX) + "," + String(message.data[2], HEX) + "," + String(message.data[3], HEX) + "," + String(message.data[4], HEX) + "," + String(message.data[5], HEX) + "," + String(message.data[6], HEX) + "," + String(message.data[7], HEX) + "\n");
    delay(1000);
  }
}
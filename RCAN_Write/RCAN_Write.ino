#include "driver/twai.h"

twai_message_t message;
twai_message_t message2;
String user = "";
void setup(){
  Serial.begin(115200);
  twai_general_config_t g_config = TWAI_GENERAL_CONFIG_DEFAULT(GPIO_NUM_39, GPIO_NUM_38, TWAI_MODE_NORMAL);
  twai_timing_config_t t_config = TWAI_TIMING_CONFIG_500KBITS();
  twai_filter_config_t f_config = TWAI_FILTER_CONFIG_ACCEPT_ALL();
  twai_driver_install(&g_config, &t_config, &f_config);
  twai_start();
}

void send_msg()
{
  message.identifier = 0x221;
  message.data_length_code = 8;
  for (int i = 0;i<message.data_length_code ; i++)
  {
    message.data[i] = i * 10;
  }
  message2.identifier = 0x121;
  message2.data_length_code = 8;
  for (int i = 0;i<message2.data_length_code ; i++)
  {
    message2.data[i] = i * 2;
  }
}

void loop(){

  delay(1000);
  if(Serial.read() != 'q' && user != "q")
  {
    if (twai_transmit(&message,1000) == ESP_OK && twai_transmit(&message2,1000) == ESP_OK )
    {
      send_msg();
      Serial.println("Sent");
    }
  }
  else{
    if (Serial.read() == 'r')
    {
      Serial.println("r received");
      user = "";

    }
    else{
      user = "q";
      Serial.println("Stopped");
    }
    
  }
  
}
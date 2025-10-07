#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  mpu.initialize();
  if (!mpu.testConnection()) {
    Serial.println("MPU6050 connection failed!");
    while (1);
  }
}

void loop() {
  int16_t ax, ay, az;
  int16_t gx, gy, gz;

  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

  // Convert raw data to degrees
  float pitch = atan2(ax, sqrt(ay*ay + az*az)) * 180 / PI;
  float roll  = atan2(ay, sqrt(ax*ax + az*az)) * 180 / PI;
  float yaw   = atan2(sqrt(ax*ax + ay*ay), az) * 180 / PI;

  Serial.print(pitch); Serial.print(",");
  Serial.print(roll); Serial.print(",");
  Serial.println(yaw);

  delay(50); // 20Hz sampling rate
}

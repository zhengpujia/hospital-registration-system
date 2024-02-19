# Generated by Django 4.2.5 on 2024-01-01 12:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hospital", "0008_doctor_registration_price_register_out_trade_num_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CheckInRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(verbose_name="打卡时间")),
                ("name", models.CharField(max_length=10, verbose_name="医生姓名")),
            ],
            options={
                "verbose_name": "签到记录",
                "verbose_name_plural": "签到记录",
            },
        ),
        migrations.AlterField(
            model_name="timenumber",
            name="default_number",
            field=models.PositiveSmallIntegerField(
                blank=True, default=10, verbose_name="默认一个时间点可预约人数"
            ),
        ),
        migrations.AlterField(
            model_name="timenumber",
            name="eight",
            field=models.PositiveSmallIntegerField(
                blank=True, default=10, verbose_name="八点可预约人数"
            ),
        ),
        migrations.AlterField(
            model_name="timenumber",
            name="eleven",
            field=models.PositiveSmallIntegerField(
                blank=True, default=10, verbose_name="十一点可预约人数"
            ),
        ),
        migrations.AlterField(
            model_name="timenumber",
            name="fifteen",
            field=models.PositiveSmallIntegerField(
                blank=True, default=10, verbose_name="十五点可预约人数"
            ),
        ),
        migrations.AlterField(
            model_name="timenumber",
            name="fourteen",
            field=models.PositiveSmallIntegerField(
                blank=True, default=10, verbose_name="十四点可预约人数"
            ),
        ),
        migrations.AlterField(
            model_name="timenumber",
            name="nine",
            field=models.PositiveSmallIntegerField(
                blank=True, default=10, verbose_name="九点可预约人数"
            ),
        ),
        migrations.AlterField(
            model_name="timenumber",
            name="seventeen",
            field=models.PositiveSmallIntegerField(
                blank=True, default=10, verbose_name="十七点可预约人数"
            ),
        ),
        migrations.AlterField(
            model_name="timenumber",
            name="sixteen",
            field=models.PositiveSmallIntegerField(
                blank=True, default=10, verbose_name="十六点可预约人数"
            ),
        ),
        migrations.AlterField(
            model_name="timenumber",
            name="ten",
            field=models.PositiveSmallIntegerField(
                blank=True, default=10, verbose_name="十点可预约人数"
            ),
        ),
    ]

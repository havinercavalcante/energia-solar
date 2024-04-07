from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption_range', models.CharField(max_length=50, verbose_name='Faixa de Consumo')),
                ('consumer_type', models.CharField(choices=[('Residencial', 'Residencial'), ('Comercial', 'Comercial'), ('Industrial', 'Industrial')], max_length=50, verbose_name='Tipo de Consumidor')),
                ('cover_value', models.FloatField(verbose_name='Valor de Cobertura')),
                ('discount_value', models.FloatField(verbose_name='Valor do Desconto')),
            ],
        ),
        migrations.AddField(
            model_name='consumer',
            name='discount_rule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='calculator.discountrule'),
        ),
    ]
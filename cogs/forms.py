import nextcord
from nextcord.ext import commands


class enrolment(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        client = self.client
        ###Создание модалов###
        class Control(nextcord.ui.Modal):
            def __init__(self):
                super().__init__('Должность Control')

                self.EmTitle = nextcord.ui.TextInput(label = 'Ваше имя и возраст', min_length=4, max_length=50, required=True, placeholder='Георгий, 18 лет', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmTitle)

                self.EmDescription = nextcord.ui.TextInput(label = 'Ваш часовой пояс', min_length=3, max_length=10, required=True, placeholder='МСК', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmDescription)

                self.EmFooter = nextcord.ui.TextInput(label = 'Расскажите о себе и почему именно вы?', min_length=25, max_length=500, required=True, placeholder='Я довольно трудолюбивый! Я считаю что именно я должен попасть на эту должность.', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmFooter)

                self.EmFooter1 = nextcord.ui.TextInput(label = 'Работал ли ты на каком либо сервере?', min_length=10, max_length=500, required=True, placeholder='Работал ранее на проекте Takizawa', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmFooter1)



                


            async def callback(self, interaction: nextcord.Interaction) -> None:
                title = self.EmTitle.value
                description = self.EmDescription.value
                footer = self.EmFooter.value
                footer1 = self.EmFooter1.value
                channel = client.get_channel(1065805820228542544)
                ### Отправка в чат ###
                emb = nextcord.Embed(title='— Пришла анкета на должность Control', description=f'・**Name + Discriminator** - {interaction.user}\n・**Mention:** - {interaction.user.mention}\n・**ID:** - {interaction.user.id}', color = 0x2f3136)
                emb.add_field(name='1. Ваше имя и возраст', value=f'{title}', inline=False)
                emb.add_field(name='2. Ваш часовой пояс', value=f'{description}', inline=False)
                emb.add_field(name='3. Расскажите о себе и почему именно вы?', value=f'{footer}', inline=False)
                emb.add_field(name='4. Работал ли ты на каком либо сервере?', value=f'{footer1}', inline=False)
                emb.set_thumbnail(url=interaction.user.avatar.url)
                await channel.send('<@!593050981969952768>,<@!640134467691741187>', embed=emb)
                emb1 = nextcord.Embed(title='— Анкета на должность Control', color = 0x2f3136)
                emb1.add_field(name='1. Ваше имя и возраст', value=f'{title}', inline=False)
                emb1.add_field(name='2. Ваш часовой пояс', value=f'{description}', inline=False)
                emb1.add_field(name='3. Расскажите о себе и почему именно вы?', value=f'{footer}', inline=False)
                emb1.add_field(name='4. Работал ли ты на каком либо сервере?', value=f'{footer1}', inline=False)
                emb1.set_thumbnail(url=interaction.user.avatar.url)
                await interaction.send(embed=emb1, ephemeral = True)

        class Support(nextcord.ui.Modal):
            def __init__(self):
                super().__init__('Должность Support')

                self.EmTitle = nextcord.ui.TextInput(label = 'Ваше имя и возраст', min_length=4, max_length=50, required=True, placeholder='Георгий, 18 лет', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmTitle)

                self.EmDescription = nextcord.ui.TextInput(label = 'Ваш часовой пояс', min_length=3, max_length=10, required=True, placeholder='МСК', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmDescription)

                self.EmFooter = nextcord.ui.TextInput(label = 'Расскажите о себе и почему именно вы?', min_length=25, max_length=500, required=True, placeholder='Я довольно трудолюбивый! Я считаю что именно я должен попасть на эту должность.', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmFooter)

                self.EmFooter1 = nextcord.ui.TextInput(label = 'Работал ли ты на каком либо сервере?', min_length=10, max_length=50, required=True, placeholder='Работал ранее на проекте Takizawa', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmFooter1)



                




            async def callback(self, interaction: nextcord.Interaction) -> None:
                title = self.EmTitle.value
                description = self.EmDescription.value
                footer = self.EmFooter.value
                footer1 = self.EmFooter1.value
                channel = client.get_channel(1065805971282198538)
                ### Отправка в чат ###
                emb = nextcord.Embed(title='— Пришла анкета на должность Support', description=f'・**Name + Discriminator** - {interaction.user}\n・**Mention:** - {interaction.user.mention}\n・**ID:** - {interaction.user.id}', color = 0x2f3136)
                emb.add_field(name='1. Ваше имя и возраст', value=f'{title}', inline=False)
                emb.add_field(name='2. Ваш часовой пояс', value=f'{description}', inline=False)
                emb.add_field(name='3. Расскажите о себе и почему именно вы?', value=f'{footer}', inline=False)
                emb.add_field(name='4. Работал ли ты на каком либо сервере?', value=f'{footer1}', inline=False)
                emb.set_thumbnail(url=interaction.user.avatar.url)
                await channel.send('<@!746613880096030741>,<@!447806409351102490>', embed=emb)
                emb1 = nextcord.Embed(title='— Анкета на должность Support', color = 0x2f3136)
                emb1.add_field(name='1. Ваше имя и возраст', value=f'{title}', inline=False)
                emb1.add_field(name='2. Ваш часовой пояс', value=f'{description}', inline=False)
                emb1.add_field(name='3. Расскажите о себе и почему именно вы?', value=f'{footer}', inline=False)
                emb1.add_field(name='4. Работал ли ты на каком либо сервере?', value=f'{footer1}', inline=False)
                emb1.set_thumbnail(url=interaction.user.avatar.url)
                await interaction.send(embed=emb1, ephemeral = True)


        class Eventsmod(nextcord.ui.Modal):
            def __init__(self):
                super().__init__('Должность Eventsmod')

                self.EmTitle = nextcord.ui.TextInput(label = 'Ваше имя и возраст', min_length=4, max_length=50, required=True, placeholder='Георгий, 18 лет', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmTitle)

                self.EmDescription = nextcord.ui.TextInput(label = 'Ваш часовой пояс', min_length=3, max_length=10, required=True, placeholder='МСК', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmDescription)

                self.EmFooter = nextcord.ui.TextInput(label = 'Расскажите о себе и почему именно вы?', min_length=25, max_length=500, required=True, placeholder='Я довольно трудолюбивый! Я считаю что именно я должен попасть на эту должность.', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmFooter)

                self.EmFooter1 = nextcord.ui.TextInput(label = 'Работал ли ты на каком либо сервере?', min_length=10, max_length=500, required=True, placeholder='Работал ранее на проекте Takizawa', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmFooter1)




                


            async def callback(self, interaction: nextcord.Interaction) -> None:
                title = self.EmTitle.value
                description = self.EmDescription.value
                footer = self.EmFooter.value
                footer1 = self.EmFooter1.value
                channel = client.get_channel(1066404967814004736)
                ### Отправка в чат ###
                emb = nextcord.Embed(title='— Пришла анкета на должность EventsMod', description=f'・**Name + Discriminator** - {interaction.user}\n・**Mention:** - {interaction.user.mention}\n・**ID:** - {interaction.user.id}', color = 0x2f3136)
                emb.add_field(name='1. Ваше имя и возраст', value=f'{title}', inline=False)
                emb.add_field(name='2. Ваш часовой пояс', value=f'{description}', inline=False)
                emb.add_field(name='3. Расскажите о себе и почему именно вы?', value=f'{footer}', inline=False)
                emb.add_field(name='4. Работал ли ты на каком либо сервере?', value=f'{footer1}', inline=False)
                emb.set_thumbnail(url=interaction.user.avatar.url)
                await channel.send('<@!644543894494642176>, <@!644543894494642176>', embed=emb)
                emb1 = nextcord.Embed(title='— Анкета на должность EventsMod', color = 0x2f3136)
                emb1.add_field(name='1. Ваше имя и возраст', value=f'{title}', inline=False)
                emb1.add_field(name='2. Ваш часовой пояс', value=f'{description}', inline=False)
                emb1.add_field(name='3. Расскажите о себе и почему именно вы?', value=f'{footer}', inline=False)
                emb1.add_field(name='4. Работал ли ты на каком либо сервере?', value=f'{footer1}', inline=False)
                emb1.set_thumbnail(url=interaction.user.avatar.url)
                await interaction.send(embed=emb1, ephemeral = True)

        class TribuneMod(nextcord.ui.Modal):
            def __init__(self):
                super().__init__('Должность EventsMod')

                self.EmTitle = nextcord.ui.TextInput(label = 'Ваше имя и возраст', min_length=4, max_length=50, required=True, placeholder='Георгий, 18 лет', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmTitle)

                self.EmDescription = nextcord.ui.TextInput(label = 'Ваш часовой пояс', min_length=3, max_length=10, required=True, placeholder='МСК', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmDescription)

                self.EmFooter = nextcord.ui.TextInput(label = 'Расскажите о себе и почему именно вы?', min_length=25, max_length=500, required=True, placeholder='Я довольно трудолюбивый! Я считаю что именно я должен попасть на эту должность.', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmFooter)

                self.EmFooter1 = nextcord.ui.TextInput(label = 'Работал ли ты на каком либо сервере?', min_length=10, max_length=50, required=True, placeholder='Работал ранее на проекте Takizawa', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmFooter1)



                




            async def callback(self, interaction: nextcord.Interaction) -> None:
                title = self.EmTitle.value
                description = self.EmDescription.value
                footer = self.EmFooter.value
                footer1 = self.EmFooter1.value
                channel = client.get_channel(1074806556039843921)
                ### Отправка в чат ###
                emb = nextcord.Embed(title='— Пришла анкета на должность TribuneMod', description=f'・**Name + Discriminator** - {interaction.user}\n・**Mention:** - {interaction.user.mention}\n・**ID:** - {interaction.user.id}', color = 0x2f3136)
                emb.add_field(name='1. Ваше имя и возраст', value=f'{title}', inline=False)
                emb.add_field(name='2. Ваш часовой пояс', value=f'{description}', inline=False)
                emb.add_field(name='3. Расскажите о себе и почему именно вы?', value=f'{footer}', inline=False)
                emb.add_field(name='4. Работал ли ты на каком либо сервере?', value=f'{footer1}', inline=False)
                emb.set_thumbnail(url=interaction.user.avatar.url)
                await channel.send('<@!843081998528020530>, <@!707639719885799444>', embed=emb)
                emb1 = nextcord.Embed(title='— Анкета на должность TribuneMod', color = 0x2f3136)
                emb1.add_field(name='1. Ваше имя и возраст', value=f'{title}', inline=False)
                emb1.add_field(name='2. Ваш часовой пояс', value=f'{description}', inline=False)
                emb1.add_field(name='3. Расскажите о себе и почему именно вы?', value=f'{footer}', inline=False)
                emb1.add_field(name='4. Работал ли ты на каком либо сервере?', value=f'{footer1}', inline=False)
                emb1.set_thumbnail(url=interaction.user.avatar.url)
                await interaction.send(embed=emb1, ephemeral = True)





        class Redactor(nextcord.ui.Modal):
            def __init__(self):
                super().__init__('Должность Redactor')

                self.EmTitle = nextcord.ui.TextInput(label = 'Ваше имя и возраст', min_length=4, max_length=50, required=True, placeholder='Георгий, 18 лет', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmTitle)

                self.EmDescription = nextcord.ui.TextInput(label = 'Ваш часовой пояс', min_length=3, max_length=10, required=True, placeholder='МСК', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmDescription)

                self.EmFooter = nextcord.ui.TextInput(label = 'Расскажите о себе и почему именно вы?', min_length=25, max_length=500, required=True, placeholder='Я довольно трудолюбивый! Я считаю что именно я должен попасть на эту должность.', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmFooter)

                self.EmFooter1 = nextcord.ui.TextInput(label = 'Работал ли ты на каком либо сервере?', min_length=10, max_length=500, required=True, placeholder='Работал ранее на проекте Takizawa', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmFooter1)



            async def callback(self, interaction: nextcord.Interaction) -> None:
                title = self.EmTitle.value
                description = self.EmDescription.value
                footer = self.EmFooter.value
                footer1 = self.EmFooter1.value
                channel = client.get_channel(1079101385871736963)
                ### Отправка в чат ###
                emb = nextcord.Embed(title='— Пришла анкета на должность Redactor', description=f'・**Name + Discriminator** - {interaction.user}\n・**Mention:** - {interaction.user.mention}\n・**ID:** - {interaction.user.id}', color = 0x2f3136)
                emb.add_field(name='1. Ваше имя и возраст', value=f'{title}', inline=False)
                emb.add_field(name='2. Ваш часовой пояс', value=f'{description}', inline=False)
                emb.add_field(name='3. Расскажите о себе и почему именно вы?', value=f'{footer}', inline=False)
                emb.add_field(name='4. Работал ли ты на каком либо сервере?', value=f'{footer1}', inline=False)
                emb.set_thumbnail(url=interaction.user.avatar.url)
                await channel.send('<@!1043547005756112966>, <@!1043547005756112966>', embed=emb)
                emb1 = nextcord.Embed(title='— Анкета на должность Redactor', color = 0x2f3136)
                emb1.add_field(name='1. Ваше имя и возраст', value=f'{title}', inline=False)
                emb1.add_field(name='2. Ваш часовой пояс', value=f'{description}', inline=False)
                emb1.add_field(name='3. Расскажите о себе и почему именно вы?', value=f'{footer}', inline=False)
                emb1.add_field(name='4. Работал ли ты на каком либо сервере?', value=f'{footer1}', inline=False)
                emb1.set_thumbnail(url=interaction.user.avatar.url)
                await interaction.send(embed=emb1, ephemeral = True)







        class Closemod(nextcord.ui.Modal):
            def __init__(self):
                super().__init__('Должность CloseMod')

                self.EmTitle = nextcord.ui.TextInput(label = 'Ваше имя и возраст', min_length=4, max_length=50, required=True, placeholder='Георгий, 18 лет', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmTitle)

                self.EmDescription = nextcord.ui.TextInput(label = 'Ваш часовой пояс', min_length=3, max_length=10, required=True, placeholder='МСК', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmDescription)

                self.EmFooter = nextcord.ui.TextInput(label = 'Расскажите о себе и почему именно вы?', min_length=25, max_length=500, required=True, placeholder='Я довольно трудолюбивый! Я считаю что именно я должен попасть на эту должность.', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmFooter)

                self.EmFooter1 = nextcord.ui.TextInput(label = 'Работал ли ты на каком либо сервере?', min_length=10, max_length=500, required=True, placeholder='Работал ранее на проекте Takizawa', style=nextcord.TextInputStyle.paragraph)
                self.add_item(self.EmFooter1)



            async def callback(self, interaction: nextcord.Interaction) -> None:
                title = self.EmTitle.value
                description = self.EmDescription.value
                footer = self.EmFooter.value
                footer1 = self.EmFooter1.value
                channel = client.get_channel(1079101385871736963)
                ### Отправка в чат ###
                emb = nextcord.Embed(title='— Пришла анкета на должность CloseMod', description=f'・**Name + Discriminator** - {interaction.user}\n・**Mention:** - {interaction.user.mention}\n・**ID:** - {interaction.user.id}', color = 0x2f3136)
                emb.add_field(name='1. Ваше имя и возраст', value=f'{title}', inline=False)
                emb.add_field(name='2. Ваш часовой пояс', value=f'{description}', inline=False)
                emb.add_field(name='3. Расскажите о себе и почему именно вы?', value=f'{footer}', inline=False)
                emb.add_field(name='4. Работал ли ты на каком либо сервере?', value=f'{footer1}', inline=False)
                emb.set_thumbnail(url=interaction.user.avatar.url)
                await channel.send('<@!1043547005756112966>, <@!1043547005756112966>', embed=emb)
                emb1 = nextcord.Embed(title='— Анкета на должность CloseMod', color = 0x2f3136)
                emb1.add_field(name='1. Ваше имя и возраст', value=f'{title}', inline=False)
                emb1.add_field(name='2. Ваш часовой пояс', value=f'{description}', inline=False)
                emb1.add_field(name='3. Расскажите о себе и почему именно вы?', value=f'{footer}', inline=False)
                emb1.add_field(name='4. Работал ли ты на каком либо сервере?', value=f'{footer1}', inline=False)
                emb1.set_thumbnail(url=interaction.user.avatar.url)
                await interaction.send(embed=emb1, ephemeral = True)






                
        
        ###Создание списка для модалов###
        class enrol_dop(nextcord.ui.Select):
            def __init__(self):
                selectOptions = [

                    nextcord.SelectOption(label='Control', emoji = '<:1103638002267332638:1170001859730214992>'),
                    nextcord.SelectOption(label='Support', emoji = '<:1103638002267332638:1170001859730214992>'),
                    nextcord.SelectOption(label='Eventsmod', emoji = '<:1103638002267332638:1170001859730214992>'),
                    nextcord.SelectOption(label='TribuneMod', emoji = '<:1103638002267332638:1170001859730214992>'),
                    nextcord.SelectOption(label='CloseMod', emoji = '<:1103638002267332638:1170001859730214992>'),
                ]
                super().__init__(placeholder='Выбери желаемую должность', min_values=1, max_values=1, options=selectOptions)


            async def callback(self, interaction: nextcord.Interaction):

                if self.values[0] == 'Control':
                    await interaction.response.send_modal(Control())
                elif self.values[0] == 'Support':
                    await interaction.response.send_modal(Support())
                elif self.values[0] == 'Eventsmod':
                    await interaction.response.send_modal(Eventsmod())
                elif self.values[0] == 'TribuneMod':
                    await interaction.response.send_modal(TribuneMod())
                elif self.values[0] == 'CloseMod':
                    await interaction.response.send_modal(Closemod())

        ### класс для списка ###
        class enrol(nextcord.ui.View):
            def __init__(self):
                super().__init__(timeout=None)
                self.add_item(enrol_dop())
        
        ### Отправка в чат наборов###
        ch = self.client.get_channel(1169999882040393852)
        await ch.purge(limit=100)
        embed=nextcord.Embed(title="Набор на должности сервера!", description = '— Чтобы оставить заявку, **воспользуйтесь** кнопками ниже и **заполните** форму.\n\n```⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Требования```\n<:dot:1066885460208660521>   Грамотность\n<:dot:1066885460208660521>   Полных **14** лет (**Исключение, EventsMod - 16+**)\n<:dot:1066885460208660521>   Стрессоустойчивость\n<:dot:1066885460208660521>   Свободное время\n\n```⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Что вас ждёт```\n<:dot:1066885460208660521>   Приятное времяпровождение в **дружном** коллективе\n<:dot:1066885460208660521>   Возможность получить **ценный** опыт и **карьерный** рост\n<:dot:1066885460208660521>   Еженедельная зарплата в виде **серверной валюты.**', color=0x2f3136)
        embed.set_image(url='https://media.discordapp.net/attachments/1057751222083399810/1062134440832278589/staff.gif')
        embed.set_footer(text = 'Проверка заявок происходит круглосуточно')
        await ch.send(embed=embed, view = enrol())




        
def setup(client):
    client.add_cog(enrolment(client))

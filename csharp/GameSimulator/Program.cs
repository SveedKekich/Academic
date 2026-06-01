using System;

namespace GameSimulator
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;

            Console.WriteLine("=== СТВОРЕННЯ ПРИСТРОЇВ ТА ІГОР ===");
            
            Device winPC = new Device("Ігровий ПК (Windows)", PlatformType.WindowsPC, new HardwareSpecs(8, 16, 6, 500), 500);
            Device phone = new Device("iPhone 15", PlatformType.Mobile, new HardwareSpecs(6, 8, 0, 128), 128);
            Device tv = new Device("Smart TV", PlatformType.Console, new HardwareSpecs(4, 4, 0, 32), 32);

            IGame civilization = new StrategyGame("Civilization VI", new HardwareSpecs(4, 8, 2, 40));
            IGame witcher = new RpgGame("The Witcher 3", new HardwareSpecs(6, 12, 4, 60));
            IGame cyberpunk = new RpgGame("Cyberpunk 2077", new HardwareSpecs(6 ,12 ,4 , 60));
            IGame StardewValley = new AdventureGame("Stardew Valley", new HardwareSpecs(2, 2, 0, 2));

            ConsoleNotificationService.SubscribeToDevice(winPC);
            ConsoleNotificationService.SubscribeToDevice(phone);
            ConsoleNotificationService.SubscribeToGame(civilization);
            ConsoleNotificationService.SubscribeToGame(witcher);
            ConsoleNotificationService.SubscribeToGame(cyberpunk);
            ConsoleNotificationService.SubscribeToGame(StardewValley);

            Console.WriteLine("\n=== ТЕСТ 1: СПРОБА ЗАПУСТИТИ БЕЗ ІНСТАЛЯЦІЇ ===");
            winPC.PlayGame(witcher, "Gamer123");

            Console.WriteLine("\n=== ТЕСТ 2: ІНСТАЛЯЦІЯ ТА ОБМЕЖЕННЯ ПАМ'ЯТІ ===");
            phone.InstallGame(witcher); 
            phone.InstallGame(civilization); 
            phone.InstallGame(cyberpunk);
            
            Console.WriteLine("\n=== ТЕСТ 3: ЗАПУСК СТРАТЕГІЇ НА ТЕЛЕФОНІ (ПЛАТФОРМЕНЕ ОБМЕЖЕННЯ) ===");
            phone.InstallGame(civilization);
            phone.PlayGame(civilization, "MobileUser"); 

            Console.WriteLine("\n=== ТЕСТ 4: УСПІШНИЙ ЗАПУСК, СЕЙВИ ТА ЛОГІН НА ПК ===");
            winPC.InstallGame(witcher);
            winPC.PlayGame(witcher, "Geralt_UA");
            
            witcher.LoadProgress(); 
            witcher.SaveProgress(); 
            witcher.LoadProgress(); 

            Console.WriteLine("\n=== ТЕСТ 5: ОДНОЧАСНИЙ ЗАПУСК ДВОХ ІГОР ===");
            winPC.PlayGame(civilization, "Geralt_UA"); 

            Console.WriteLine("\n=== ТЕСТ 6: ЗАКРИТТЯ ГРИ ТА МУЛЬТИПЛЕЄР RPG ===");
            winPC.StopCurrentGame();
            
            winPC.PlayGame(witcher, "Geralt_UA");
            var rpgGame = (RpgGame)witcher;
            rpgGame.SetupMultiplayer(winPC.ConnectedControllers); 
            
            winPC.ConnectControllers(3); 
            rpgGame.SetupMultiplayer(winPC.ConnectedControllers); 

            Console.WriteLine("\n=== ТЕСТ 7: СТРІМІНГ З МОБІЛЬНОГО ===");
            phone.StreamToDevice(tv);  
            winPC.StreamToDevice(tv);  

            winPC.StopCurrentGame();
            Console.WriteLine("\nСимуляцію завершено. Натисніть будь-яку клавішу...");
            Console.ReadKey();
        }
    }
} 
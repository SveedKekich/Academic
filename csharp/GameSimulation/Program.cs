using System;
using GameSimulation.Domain;
using GameSimulation.Domain.Enums;
using GameSimulation.Domain.Models;
using GameSimulation.Infrastructure;
using GameSimulation.Patterns.Strategy;

namespace GameSimulation
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("=== СИМУЛЯТОР КОМП'ЮТЕРНИХ ІГОР ===");

            Device PC = new Device(DevicePlatform.WindowsPC, new HardwareSpecs(8, 16, 8, 500));
            Device Phone = new Device(DevicePlatform.Mobile, new HardwareSpecs(4, 6, 2, 64));
            Device WeakPC = new Device(DevicePlatform.WindowsPC, new HardwareSpecs(2, 4, 1, 200));

            Game starcraft = new Game("StarCraft II", GameGenre.Strategy, new HardwareSpecs(4, 8, 2, 30), new WindowsOnlyStrategy());
            Game witcher = new Game("The Witcher 3", GameGenre.RPG, new HardwareSpecs(6, 12, 4, 50), new CrossPlatformStrategy(), isMultiplayerSupported: true);
            Game badGame = new Game("Unoptimized Game", GameGenre.Adventure, new HardwareSpecs(16, 64, 24, 600), new CrossPlatformStrategy());

            Player player = new Player("Олексій");
            player.AddGameToLibrary(starcraft);
            player.AddGameToLibrary(witcher);
            player.AddGameToLibrary(badGame);

            Console.WriteLine("\n--- Тест 1: Перевірка сумісності (Стратегія на Mobile) ---");
            starcraft.Install(Phone);

            Console.WriteLine("\n--- Тест 2: Перевірка нестачі місця на HDD ---");
            badGame.Install(PC); 

            Console.WriteLine("\n--- Тест 3: Спроба маніпуляцій з неінстальованою грою ---");
            witcher.Launch(PC);
            witcher.Load();

            Console.WriteLine("\n--- Тест 4: Успішна інсталяція та Спроба запуску на слабкому ПК ---");
            witcher.Install(WeakPC); 
            witcher.Launch(WeakPC);   

            Console.WriteLine("\n--- Тест 5: Повний життєвий цикл на потужному ПК (State + Observer) ---");
            witcher.Install(PC);
            player.PlayGame(witcher, PC); 
            
            Console.WriteLine("\n--- Тест 6: Спроба завантаження без авторизації та сейвів ---");
            witcher.Load();
            witcher.Login();
            witcher.Load(); 
            witcher.Save(); 
            witcher.Load(); 

            Console.WriteLine("\n--- Тест 7: Обмеження одночасної гри в дві гри ---");
            player.PlayGame(starcraft, PC); 

            Console.WriteLine("\n--- Тест 8: RPG Мультиплеєр та Маніпулятори ---");
            witcher.StartMultiplayer(1); 
            witcher.StartMultiplayer(3); 

            Console.WriteLine("\n--- Тест 9: Закриття гри та запуск іншої ---");
            player.StopCurrentGame();
            starcraft.Install(PC);
            player.PlayGame(starcraft, PC); 

            Console.WriteLine("\n--- Тест 10: Трансляція з мобільного пристрою ---");
            Phone.StreamToOtherDevice();
            PC.StreamToOtherDevice();

            Console.ReadLine();
        }
    }
}
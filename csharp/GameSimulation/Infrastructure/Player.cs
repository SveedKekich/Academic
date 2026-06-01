using System;
using System.Collections.Generic;
using GameSimulation.Domain;
using GameSimulation.Domain.Enums;
using GameSimulation.Domain.Models;
using GameSimulation.Patterns.Observer;

namespace GameSimulation.Infrastructure
{
    public class Player
    {
        public string Name { get; }
        public List<Game> Library { get; } = new List<Game>();
        private Game? _currentlyPlaying = null;

        public Player(string name)
        {
            Name = name;
        }

        public void AddGameToLibrary(Game game)
        {
            Library.Add(game);
            game.OnGameEvent += HandleGameNotification; 
        }

        private void HandleGameNotification(object? sender, GameEventArgs e)
        {
            var oldColor = Console.ForegroundColor;
            Console.ForegroundColor = e.Type switch
            {
                GameNotificationType.Success => ConsoleColor.Green,
                GameNotificationType.Warning => ConsoleColor.Yellow,
                GameNotificationType.Error => ConsoleColor.Red,
                _ => ConsoleColor.White
            };
            Console.WriteLine(e.Message);
            Console.ForegroundColor = oldColor;
        }

        public void PlayGame(Game game, Device device)
        {
            if (_currentlyPlaying != null && _currentlyPlaying != game && _currentlyPlaying.IsRunning)
            {
                Console.WriteLine($"[Система] Помилка: Гравець вже грає в '{_currentlyPlaying.Title}'. Спочатку закрийте її.");
                return;
            }

            if (!game.IsRunning)
            {
                game.Launch(device);
                if (game.IsRunning)
                {
                    _currentlyPlaying = game;
                }
            }
        }

        public void StopCurrentGame()
        {
            if (_currentlyPlaying != null)
            {
                _currentlyPlaying.Close();
                _currentlyPlaying = null;
            }
        }
    }
}
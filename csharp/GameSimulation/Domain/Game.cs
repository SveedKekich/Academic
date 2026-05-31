using System;
using GameSimulation.Domain.Enums;
using GameSimulation.Domain.Models;
using GameSimulation.Patterns.Observer;
using GameSimulation.Patterns.State;
using GameSimulation.Patterns.Strategy;

namespace GameSimulation.Domain
{
    public class Game
    {
        private IGameState _state;
        
        public string Title { get; }
        public GameGenre Genre { get; }
        public HardwareSpecs Requirements { get; }
        public ICompatibilityStrategy Compatibility { get; }
        
        public bool IsLoggedIn { get; internal set; }
        public bool HasSaves { get; internal set; }
        public bool IsMultiplayerSupported { get; private set; }

        public event EventHandler<GameEventArgs>? OnGameEvent;

        public Game(string title, GameGenre genre, HardwareSpecs requirements, ICompatibilityStrategy compatibility, bool isMultiplayerSupported = false)
        {
            Title = title;
            Genre = genre;
            Requirements = requirements;
            Compatibility = compatibility;
            IsMultiplayerSupported = isMultiplayerSupported;
            _state = new NotInstalledState();
        }

        public void ChangeState(IGameState state) => _state = state;

        public void Notify(string message, GameNotificationType type)
        {
            OnGameEvent?.Invoke(this, new GameEventArgs($"[{Title}] {message}", type));
        }

        public void Install(Device device) => _state.Install(this, device);
        public void Launch(Device device) => _state.Launch(this, device);
        public void Login() => _state.Login(this);
        public void Save() => _state.Save(this);
        public void Load() => _state.Load(this);
        public void Close() => _state.Close(this);

        public bool IsRunning => _state is LaunchedState;

        public void StartMultiplayer(int connectedControllers)
        {
            if (!IsRunning)
            {
                Notify("Неможливо активувати мультиплеєр. Гра не запущена.", GameNotificationType.Error);
                return;
            }
            if (!IsMultiplayerSupported)
            {
                Notify("Ця гра не підтримує мультиплеєр.", GameNotificationType.Error);
                return;
            }
            if (connectedControllers < 2)
            {
                Notify("Мультиплеєр недоступний: підключено недостатньо маніпуляторів (потрібно мін. 2).", GameNotificationType.Warning);
                return;
            }

            Notify($"Мультиплеєр активовано для {connectedControllers} гравців!", GameNotificationType.Success);
        }
    }
}
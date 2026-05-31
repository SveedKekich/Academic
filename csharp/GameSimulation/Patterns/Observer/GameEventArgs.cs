using System;
using GameSimulation.Domain.Enums;

namespace GameSimulation.Patterns.Observer
{
    public class GameEventArgs : EventArgs
    {
        public string Message { get; }
        public GameNotificationType Type { get; }

        public GameEventArgs(string message, GameNotificationType type)
        {
            Message = message;
            Type = type;
        }
    }
}
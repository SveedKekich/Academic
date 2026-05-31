using System;

namespace GameSimulator
{
    // Аргументи подій для відірваності UI від логіки
    public class GameEventArgs : EventArgs
    {
        public string Message { get; set; }
        public GameEventArgs(string message) => Message = message;
    }
}
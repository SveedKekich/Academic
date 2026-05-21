namespace MessengerApi.Models;

public class Message
{
    public Guid MessageId { get; set; } = Guid.NewGuid();

    public Guid SenderId { get; set; }

    public Guid ReceiverId { get; set; }

    public string Text { get; set; } = string.Empty;

    public DateTime Timestamp { get; set; } = DateTime.UtcNow;

    public bool IsEdited { get; set; }

    public bool DeletedForEveryone { get; set; }

    // delete only for sender
    public bool DeletedForSender { get; set; }

    // delete only for receiver
    public bool DeletedForReceiver { get; set; }
}
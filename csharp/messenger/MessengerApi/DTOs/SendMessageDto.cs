namespace MessengerApi.DTOs;

public class SendMessageDto
{
    public Guid SenderId { get; set; }

    public Guid ReceiverId { get; set; }

    public string Text { get; set; } = string.Empty;
}
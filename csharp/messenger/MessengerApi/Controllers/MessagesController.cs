using MessengerApi.DTOs;
using MessengerApi.Services;
using Microsoft.AspNetCore.Mvc;

namespace MessengerApi.Controllers;

[ApiController]
[Route("messages")]
public class MessagesController : ControllerBase
{
    private readonly MessageService _service;

    public MessagesController(MessageService service)
    {
        _service = service;
    }

    [HttpPost]
    public async Task<IActionResult> Send(SendMessageDto dto)
    {
        var result =
            await _service.SendMessage(
                dto.SenderId,
                dto.ReceiverId,
                dto.Text
            );

        if (!result.Success)
            return BadRequest(result.Error);

        return Ok(result.Message);
    }

    [HttpGet("{user1}/{user2}")]
    public async Task<IActionResult> History(
        Guid user1,
        Guid user2
    )
    {
        var messages =
            await _service.GetHistory(user1, user2);

        return Ok(messages);
    }

    [HttpPut("{messageId}")]
    public async Task<IActionResult> Edit(
        Guid messageId,
        EditMessageDto dto
    )
    {
        var success =
            await _service.EditMessage(
                messageId,
                dto.NewText
            );

        if (!success)
            return BadRequest("Cannot edit message");

        return Ok();
    }

    [HttpDelete("{messageId}/everyone")]
    public async Task<IActionResult> DeleteEveryone(
        Guid messageId
    )
    {
        var success =
            await _service.DeleteForEveryone(messageId);

        if (!success)
            return NotFound();

        return Ok();
    }
}
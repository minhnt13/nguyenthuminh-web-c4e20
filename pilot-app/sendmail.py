from gmail import GMail, Message

html_content ="""
Yêu cầu của bạn đã được xử lý, chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất. Cảm ơn bạn đã sử dụng dịch vụ của ‘Mùa Đông Không Lạnh’
"""

gmail = GMail("Minh<minhnt13@gmail.com>","someknownow")
msg = Message(
    "Xét duyệt yêu cầu - Mùa Đông Không Lạnh",
    to="imrichaf@gmail.com",
    html=html_content)

if hour_now > time_period:
    gmail.send(msg)